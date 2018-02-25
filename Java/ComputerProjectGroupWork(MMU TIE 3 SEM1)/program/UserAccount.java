// File: UserAccount.java

// File contains a class UserAccount that holds the user
// account details of one internet user.

package data.users; // own package, not part of standard java.

public class UserAccount
{
	private final String firstName;
	private final String lastName;

	private double totalBundle; // total amount of data allocated to this user.
	private double usedBundle; // total amount of data that this user has used so far.
	private int shareRatio; // what ratio of total did this user contribute?

	private String ipAddress;
	private final String macAddress; // this account belongs exclusively to the user whose device bears this MAC.

	// time that the user started using their bundle.
	// useful for calculating the total time the user will be logged in
	private long loginTime = 0;
	private long logoutTime = 0;
	private long lastUpdateTime; // time when the last account update was performed.

	public static boolean accountStatus = false; // logged into or not.

	// since the users will be stored in an array during runtime
	// keep track of the user's index in that array
	private int userArrayIndex;

	// constructor - initializes all of the above instance variables
	public UserAccount(String fname, String lname, String ip,
		String mac, double initialBundle, int ratio, int index)
	{
		firstName = fname;
		lastName = lname;
		ipAddress = ip;
		macAddress = mac;
		setTotalBundle(initialBundle);
		setShareRatio(ratio);
		setUserArrayIndex(index);
	}

	// set total bundle allocated to this user
	public void setTotalBundle(double bundle)
	{
		if(bundle > 0.0)
			totalBundle = bundle;
		else
			throw new IllegalArgumentException(
				"Bundle amount should be greater than zero.");
	}

	// add some data usage amount to the user's usedBundle
	public void addToUsedBundle(double amount)
	{
		if(amount > 0.0)
			usedBundle += amount;
		else
			throw new IllegalArgumentException(
				"Amount of data used must be greater than zero.");
	}

	// get the user's total bundle allocation
	public double getTotalBundle()
	{
		return totalBundle;
	}

	// set this user's login time
	public void setLoginTime(long time)
	{
		if(time > 0){
			loginTime = time;
			accountStatus = true;
			lastUpdateTime = loginTime; // this account was last updated when it was first logged into.
		}
		else
			throw new IllegalArgumentException(
				"Time cannot be zero or less than zero.");
	}

	// get log in time.
	public long getLoginTime()
	{
		return loginTime;
	}

	// Logout time
	public void setLogoutTime(long time)
	{
		if(time > 0){
			accountStatus = false;
			logoutTime = time;
		}
		else
			throw new IllegalArgumentException(
				"Time cannot be zero or less than zero.");
	}

	public long getLogoutTime()
	{
		return logoutTime;
	}

	// last time the account balance was updated.
	public void setLastUpdateTime(long time)
	{
		if(time > 0)
			lastUpdateTime = time;
		else
			throw new IllegalArgumentException(
				"Time cannot be zero or less than zero.");
	}

	public long getLastUpdateTime()
	{
		return lastUpdateTime;
	}

	// set the ratio of the total that the user contributed.
	public void setShareRatio(int ratio)
	{
		if(ratio > 0)
			shareRatio = ratio;
		else
			throw new IllegalArgumentException(
				"Sharing ratio must be an integer greater than zero.");
	}
	
	// set the user index in the array.
	public void setUserArrayIndex(int index)
	{
		if(index >= 0)
			userArrayIndex = index;
		else
			throw new IllegalArgumentException(
				"User index in the array cannot be negative.");
	}

	// get user index in array
	public int getUserArrayIndex()
	{
		return userArrayIndex;
	}

	// get amount of data used.
	public double getUsedBundle()
	{
		return usedBundle;
	}

	// get user names
	public String getNames()
	{
		return String.format("%s %s", firstName, lastName);
	}

	// calculate user's remaining bundle balance.
	public double getBundleBalance()
	{
		return (getTotalBundle() - getUsedBundle());
	}

	public String getIpAddress()
	{
		return ipAddress;
	}

	public String getMacAddress()
	{
		return macAddress;
	}

	@Override
	public String toString()
	{
		return String.format("%s: %s\n%s: %.2f\n%s: %.2f\n",
			"Account Holder", getNames(),
			"Allocated Bundle", getTotalBundle(),
			"Bundle Balance", getBundleBalance());
	}
}