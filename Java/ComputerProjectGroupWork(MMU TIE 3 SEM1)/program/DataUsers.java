// File: DataUsers.java

// Contains the class DataUsers that holds a detail of
// Each user has their share of the internet bundle according to some ratio.

import java.util.InputMismatchException;
import java.util.StringTokenizer;
import java.util.Scanner;

import data.users.UserAccount; // own package, not part of standard java.

public class DataUsers
{
	// specific user info
	private String firstName = "null";
	private String lastName = "null";
	private String ipAddress = "null";
	private String macAddress = "null";
	
	private double bundle; // that is being shared;
	private final double dataRate = 100; // Assumes that the user will consume this amount of data in a second, in KBytes.

	// general users info
	public static final int maxUsers = 10; // this program can handle only 10 users.
							   // public and static, visible anywhere and can be reference by name,
							   // final, cannot be modified unless manually changed here in this file.

	// users
	private UserAccount[] myUsers = new UserAccount[maxUsers];
	public static int usersAccountsCount = 0; // total number of users currently in myUsers.

	int[] ratio = new int[maxUsers]; // ratio used to share the bundle.

	private boolean accountReset = false; // whether the account has been reset or not.

	Scanner input = new Scanner(System.in);

	// constructor: make one UserAccount stored in the myUsers array.
	public DataUsers()
	{
		setBundleAmount();
		myUsers[usersAccountsCount] = new UserAccount(firstName, lastName, ipAddress, macAddress,
			0.01, 1, 0);
	}

	// Prompt user for names then set them.
	public void setNames()
	{
		// get names:
		String[] names = new String[2];
		System.out.print("\nEnter the first name followed by the last name:\n");
		System.out.print("Separate the names with a space:\n");

		do{
		    System.out.print("> ");
		    String name = input.nextLine();

		    names = name.split(" ");
		} while(names.length != 2);

		firstName = names[0];
		lastName = names[1];
	}

	// return the names currently in this class(current user being set)
	public String getNames()
	{
		return String.format("%s %s", firstName, lastName);
	}

	// return the names of a particular user in the users array.
	public String getNames(int id)
	{
		return myUsers[id].getNames();
	}

	// prompt for and set total bundle to be shared.
	public void setBundleAmount()
	{
		try{
			System.out.print("Enter the data bundle amount to be shared (in MegaBytes):\n> ");
			double amount = input.nextDouble();
			if(amount > 0.0)
				bundle = amount;
			else
				throw new IllegalArgumentException(
					"Data Bundle Amount must be greater than 0.0");

		}
		catch(InputMismatchException e){
			System.err.println("\nError: Amount needed to be a number.\nExiting.");
			System.exit(1); // quit program.
		}
		catch (IllegalArgumentException e){
			System.err.printf("\nError: %s\nExiting.\n", e.getMessage());
			System.exit(1);			
		}
	}

	// get total bundle amount
	public double getBundle()
	{
		return bundle;
	}

	// Prompt for and set the IP Address as well as the MAC address
	public void setDeviceInfo()
	{
		// Ideally should use regular expressions to ensure IP Address validity
		System.out.printf("\nEnter the IP Address for %s:\n> ", getNames());
		String ip = input.nextLine();

		// Ideally should use regex to ensure mac address's validity
		System.out.printf("\nEnter the MAC address for %s,\n e.g. 00:11:22:33:44:55\n> ", getNames());
		String mac = input.nextLine();

		mac = checkMacAddress(mac);

		int i = 0;
		boolean flag = true;
		while((myUsers[i] != null) && (i < myUsers.length)){
			if(myUsers[i].getMacAddress().equals(mac)){
				System.out.println("Invalid macAddress: that macAddress is already registered." +
					"\nPlease enter a different macAddress or login.");
				flag = false;
				break;
			}
			else
				i++;
		}

		if(flag){
			ipAddress = ip;
			macAddress = mac;
		}
		else{
			System.out.println("That MAC Address was not set.\n");
			System.out.println("User not created. Reset accounts then try again.\n");
		}
	}

	// check that the mac address is not less than 17 characters
	private String checkMacAddress(String mac)
	{
		while(mac.length() != 17){
			System.out.println("\nIncorrect input. Press Enter to try again.");
			String discard = input.nextLine();

			System.out.printf("\nEnter the MAC address for %s,\n e.g. 00:11:22:33:44:55\n> ", getNames());
			mac = input.nextLine();
		}
		return mac;
	}

	// prompt for and set the sharing ratio
	public void setSharingRatio(int number)
	{
		try{
			if (number >= 0 && number < maxUsers){
				if(number != 1){
					System.out.printf("\nEnter the sharing ratio between %d users,\n", number);
					System.out.print("e.g. if for 3 users the ratio is 3:2:1, enter 3 2 1\n> ");
					
					for(int i = 0; i < number; i++){
						ratio[i] = input.nextInt();
					}
				}
				else
					ratio[usersAccountsCount] = 1;
			}
			else
				throw new IllegalArgumentException(
					"Users number cannot be less than zero or greater than " + maxUsers);
		}
		catch(InputMismatchException e){
			System.err.println("\nError: Unexpected input.\nExiting");
			System.exit(1);
		}
		catch (IllegalArgumentException e){
			System.err.printf("\nError: %s\nExiting.\n", e.getMessage());
			System.exit(1);			
		}
	}

	// calculate the bundle allocation for user in account held in this index.
	public double calculateBundle(int accountIndex)
	{
		int totalRatio = 0;
		for(int i = 0; i < ratio.length; i++){
			if(ratio[i] > 0){
				totalRatio += ratio[i];
			}
			else
				break; // no more numbers in the ratio array.
		}

		int userRatio = ratio[accountIndex];

		double userBundle = ((double)userRatio/totalRatio) * getBundle();

		return userBundle;
	}

	// get bundle balance
	public void getBundleBalance(int index)
	{
		// Maybe the user has overused their databundle due to errors in this system? Do not let them know that.
		System.out.printf("\nAccount Bundle Balance: %.2f",
			myUsers[index].getBundleBalance() < 0.0 ? 0.0 : myUsers[index].getBundleBalance());
	}

	// Create account for one of the users who are sharing data
	public void createAccounts()
	{
		if(usersAccountsCount == 0){
			try{
				if(accountReset)
					setBundleAmount();

				System.out.print("\nCreate Accounts for how many users?\n> ");
				int users = input.nextInt();
				if(users > 0 && users < maxUsers){
					// set sharing ratio of this number of users.
					if(users == 1)
						setSharingRatio(1);
					else
						setSharingRatio(users);

					for(int i = 0; i < users; i++){
						System.out.printf("\nFor User %d:",(i + 1));
						setNames();
						setDeviceInfo();
						myUsers[usersAccountsCount] = new UserAccount(firstName, lastName, ipAddress, macAddress,
							0.01, ratio[usersAccountsCount], usersAccountsCount);

						// set the values from 0.01
						myUsers[usersAccountsCount].setTotalBundle(calculateBundle(usersAccountsCount));
						usersAccountsCount += 1; // add one to this count if one user is added to the accounts.
						// the next user will use this number, then add one to it as well for the next user
					}
				}
				else
					System.out.printf("\nNumber of users cannot be less than zero or greater than %d\n\n", maxUsers);
			}
			catch(InputMismatchException e){
				System.err.println("\nError: Unexpected input.\nExiting\n");
				System.exit(1);
			}
		}
		else{
			System.out.println("There are already users created. You have to wait until their sessions expire" +
				"\nin order for you to create other accounts.\nOr reset accounts now.");
		}
	}

	// reset user accounts (maybe sessions have expired and you want to create new user accounts?)
	public void resetAccounts()
	{
		String adminPass = "toor";
		String password;
		int trials = 0;
		do{
			String discard = input.nextLine(); // clear the buffer

			System.out.print("Enter the admin password to reset accounts.\n> ");
			password = input.nextLine();
			if(adminPass.equals(password)){
				myUsers = new UserAccount[maxUsers];
				usersAccountsCount = 0;
				accountReset = true;
				System.out.println("Accounts reset successfully");
				return;
			}
			else{
				System.out.println("Incorrent admin password.\n");
				if(trials != 2)
					System.out.println("Press Enter to try again.");
			}
			trials++;
		}while(trials < 3);

		System.out.println("Accounts not reset.");

	}

	// allow a registered user to log in
	public int login()
	{
		System.out.print("\nEnter ip address: ");
		String ip = input.nextLine();
		System.out.print("\nEnter device MAC Address: ");
		String mac = input.nextLine();
		int loops = 0;

		for(int i = 0; i < myUsers.length; i++){
			try{
				if((myUsers[i].getIpAddress().equals(ip)) &&
					(myUsers[i].getMacAddress().equals(mac)))
				{
					myUsers[i].setLoginTime(System.currentTimeMillis()); // log this users login time. (no pun intended ;) )
					
					// update this account
					updateUserAccount(i);
					return i;
				}
				loops += 1;
			}

			catch(Exception e){ // No more user accounts in array.
				if(loops == 1)
					System.out.println("\nNo accounts created. You need to create accounts first.");

				else{
					System.out.println("\nNo user registered under those credentials.");
				}
				break; // out of the for loop
			}
		}
		return -1;
	}

	// logout
	public void logout(int accountIndex)
	{
		// update the user account
		updateUserAccount(accountIndex);

		// finally, log out.
		myUsers[accountIndex].setLogoutTime(System.currentTimeMillis());
	}

	// return a string representation of any time given in milliseconds.
	private String timeString(long milliSecs)
	{
		// calculate the total seconds since epoch.
		long totalSeconds = milliSecs / 1000;

		// current second from the total seconds
		long currentSecond = totalSeconds % 60;

		// total minutes since epoch
		long totalMinutes = totalSeconds / 60;

		// current minute from total minutes
		long currentMinute = totalMinutes % 60;

		// total hours since epoch
		long totalHours = totalMinutes / 60;

		// current hour from total hours.
		long currentHour = totalHours % 24; // + 3 to make it EAT from GMT

		return String.format("%s:%s:%s GMT", 
			currentHour < 12 ? ("0" + currentHour) : currentHour,
			currentMinute < 10 ? ("0" + currentMinute) : currentMinute,
			currentSecond < 10 ? ("0" + currentSecond) : currentSecond);
	}

	// return a string representation of the login time
	public String getLoginTime(int accountIndex)
	{
		return timeString(myUsers[accountIndex].getLoginTime());
	}

	// Determine whether a user's session is valid, that is, has any bundles remaining.
	public boolean sessionIsValid(int accountIndex)
	{
		updateUserAccount(accountIndex); // subtract the amount the user has used so far during this session.

		if(myUsers[accountIndex].accountStatus){
			double remainingMbs = myUsers[accountIndex].getBundleBalance();

			// if any balance, then session is valid
			if(remainingMbs >= 0.01)
				return true;
			else
				logout(accountIndex); // no more bundles remaining, log them out.
		}

		// Execute this after the logout.
		System.out.println("\nSession Information:");
		getSessionInfo(accountIndex);
		getBundleBalance(accountIndex);
		System.out.printf("\nAccount Status: %s\n", myUsers[accountIndex].accountStatus ? "ACTIVE" : "INACTIVE");
		System.out.print("\nYour session has expired.\n");

		return false;
	}

	// update the users account. This method will constantly be called in loops in main's submenu
	public void updateUserAccount(int accountIndex)
	{
		long updateTime = System.currentTimeMillis();
		long timeElapsed =  updateTime - myUsers[accountIndex].getLastUpdateTime();

		// convert to seconds
		double timeElapsedSeconds = (timeElapsed / 1000) + 0.01; // + 0.01 to ensure that the time is never 0.0

		// data consumed in this time
		double dataConsumed = timeElapsedSeconds * (dataRate/1024); // MBytes.

		// debug
		//System.out.printf("\nIn updateUserAccount:\n");
		//System.out.println("Time elapsed in seconds: " + timeElapsedSeconds);
		//System.out.println("Amount of data consumed: " + dataConsumed);

		// add that amount to the usedBundle of the account in accountIndex.
		myUsers[accountIndex].addToUsedBundle(dataConsumed);

		// update the last time updated.(pun?:) )
		myUsers[accountIndex].setLastUpdateTime(updateTime);
	}

	//  Print out the details of this log in session.
	public void getSessionInfo(int accountIndex)
	{
		long timeNow = System.currentTimeMillis();
		long elapsedTime = timeNow - myUsers[accountIndex].getLoginTime();

		System.out.printf("%s: %s\n%s: %s\n",
			"Log in time", getLoginTime(accountIndex),
			"Elapsed time", timeString(elapsedTime));

	}

	// print info about one user.
	public String userInfo(int index)
	{
		return String.format("%s", myUsers[index].toString());
	}

	// return info about all registered users.
	@Override
	public String toString()
	{
		String usersInfo = "";
		for(int i = 0; i < myUsers.length; i++){
			if(myUsers[i] != null)
				usersInfo = usersInfo + myUsers[i].toString();
			else
				break;
		}
		return String.format("%s", usersInfo);
	}
}