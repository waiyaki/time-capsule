/*
 * The file AnnualLoan.java.
 * This file contains class AnnualLoan which extends the class Loan 
 * and is a class of Loan objects that must have
 * a payoff period of exactly 12 months.
*/

import java.util.GregorianCalendar;

public class AnnualLoan extends Loan implements LoanInterface
{
	private final int payOffMonths = 12; // Annual

	// default constructor
	public AnnualLoan()
	{
		super();
		checkPayOffMonths();
	}

	// constructor - the arguments should come in from
	// the main when instantiating this object
	public AnnualLoan(String name)
	{
		// instantiate Loan
		super(name); // call the 2 argument constructor of Loan
		checkPayOffMonths(); // ensure that for an annual loan,
							// number of months to full resettlement == 12.
	}

	// 3-arg constructor
	public AnnualLoan(String name, double amount, int months)
	{
		// instantiate Loan
		super(name, amount, months); // call the 3 argument constructor of Loan
		checkPayOffMonths(); // ensure that for an annual loan,
							// number of months to full resettlement == 12.
	}
	// get payOffMonths in annual loan object
	public int getPayOffMonths()
	{
		return payOffMonths;
	}

	// restrict annual class number of months to pay off.
	// just in case the user constructs the annual object
	// with months not equal to 12.
	public void checkPayOffMonths()
	{
		int monthsSetInMain = getPayOffMonths();
		try{
			if(monthsSetInMain != payOffMonths){
				throw new IllegalArgumentException(
					"ILLEGAL MONTHS FOR AN ANNUAL LOAN OBJECT.\n"
					+ "Months should be 12. Changing months to 12...");
			}
		}
		catch(IllegalArgumentException e){
			System.err.printf("Exception: %s", e.getMessage());
			setPayOffMonths(payOffMonths); // correct the number of months for an annual loan object
		}

	}

	@Override
	public double CalculateFee()
	{
		return getAmountLoaned() + getFee();
	}

	// convert AnnualLoan to a string representation
	@Override
	public String toString()
	{
		return String.format("%s\n%s:\t$%,.2f",
			super.toString(),
			"Total Amount To Pay", CalculateFee());
	}
}