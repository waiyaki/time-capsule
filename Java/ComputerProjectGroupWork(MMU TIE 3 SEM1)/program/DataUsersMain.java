// File: DataUsersMain.java

// File contains test program for the classes UserAccount, DataUsers.
import java.util.InputMismatchException;
import java.util.Scanner;

public class DataUsersMain
{
	public static void main(String[] args)
	{
		int accountID = -1;// Account ID of one user in the UserAccounts array.

		DataUsers users = new DataUsers(); // make an array of data users.

		// create a Scanner object
		Scanner input = new Scanner(System.in);

		String menu = "Select your choice:\n1. Create Accounts\n2. Login\n3. Reset Accounts\n4. Quit";
		String subMenu = "\n   Select your choice:\n\t1. View account information\n\t2. View Session Time information.\n\t3. Log out.";

		int choice = 0; // undefined.
		int ans = 0; // undefined.

		do{
			try{
				System.out.printf("\n%s\n> ", menu);
				String response = input.nextLine();

				try{
					choice = Integer.parseInt(response);
				}

				catch (Exception e) {
					continue;
				}

				switch(choice){
					case 1:
						accountID = users.usersAccountsCount;
						users.createAccounts();
						// debug
						//System.out.println(users.toString());
						continue;
					case 2:
						accountID = users.login();
						break;
					case 3:
						users.resetAccounts();
						continue;
					case 4:
						System.out.println("Goodbye!");
						System.exit(0);
					default:
						System.out.println("\nInvalid choice. Try again.\n");
						continue;
				} // end switch

				if(accountID >= 0){
					// Be updating the account even when waiting for user input.
					CheckSession thisSession = new CheckSession(users, accountID);

					// loop till the user logs out or their session dies.
					do{
						System.out.printf("  \nWelcome, %s", users.getNames(accountID));
						System.out.printf("%s\n> ", subMenu);
						response = input.nextLine();

						try{
							ans = Integer.parseInt(response);
						}

						catch(Exception e) {
							continue;
						}

						// is the user account still active?
						// and is the thread still alive, or the user delayed their input for so
						// long until all internet was consumed and they were logged out?
						if(thisSession.isAlive()){
							switch(ans){
								case 1:
									System.out.printf("\n%s\n", users.userInfo(accountID));
									users.getSessionInfo(accountID);
									break;
								case 2:
									System.out.println();
									users.getSessionInfo(accountID);
									break;
								case 3:
									thisSession.stop(); // stop updating this account.
									users.logout(accountID);
									break;
								default:
									System.out.println("\nUnknown option.");
							}
						}

						// if their internet session timed out, tell them this.
						if(!thisSession.isAlive()){
							System.out.printf("\nYou have been logged out.\n");
						}

					} while(ans != 3 && thisSession.isAlive());
				}
			}
			catch(InputMismatchException e){
				System.err.printf("Error: Invalid inputs.\nExiting.\n");
				System.exit(1);
			}

		} while(choice != 4);
	}
}

class CheckSession extends Thread
{
	DataUsers theUsers;
	int account;

	protected volatile boolean done = false;

	CheckSession(DataUsers theUsers, int accountID)
	{
		super("My checkSession Thread.");
		this.theUsers = theUsers;
		account = accountID;
		start();
	}

	public void shutDown()
	{
		done = true;
	}

	public void run()
	{
		while(!done){
			try{
				while(theUsers.sessionIsValid(account)){
					Thread.sleep(10000); // if the account is valid, sleep for 10 seconds before checking again.
				}
				// if the account is not valid, shutdown this thread
				shutDown();
			}
			catch (InterruptedException e){
				// Nothing to do here.	
			}
		}
	}
}