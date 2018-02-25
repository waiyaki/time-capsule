/*
 * The file Loan.java
 * Contains the class Loan, which is a class for general Loan objects
 * that can have any payoff period as specified in the fee structure.
*/

import java.util.InputMismatchException;
import java.util.GregorianCalendar;
import java.util.Scanner;

public class Loan
{
	// amounts
	private final double maxLoanAmount = 10000.00;
	private double amountLoaned;

	// dates and time
	private GregorianCalendar dateLoaned; // date loaned
	private int payOffMonths; // months to payoff the loan
	private GregorianCalendar payByDate; // date to have paid the loan back by

	// single loanee detail
	private String loaneeName;

	// Scanner object
	Scanner input = new Scanner(System.in);

	// default constructor
	public Loan()
	{
		setLoaneeName();
		System.out.printf("Loanee %s's Details:\n", getLoaneeName());
		setAmountLoaned();
		setPayOffMonths();
		setDateLoaned();
		setPayByDate();
		System.out.println(); // new line before next object's instantiation
	}

	// one argument constructor
	public Loan(String name)
	{
		System.out.printf("Loanee %s's Details:\n", name);
		setLoaneeName(name);
		setAmountLoaned();
		setPayOffMonths();
		setDateLoaned();
		setPayByDate();
		System.out.println(); // new line before next object's instantiation
	}

	// 3 argument constructor- User can pass name, months to full resettlement
	// and amount loaned here.
	public Loan(String name, double amount, int months)
	{
		setLoaneeName(name);
		setAmountLoaned(amount);
		setPayOffMonths(months);
		setDateLoaned();
		setPayByDate();
		System.out.println(); // new line before next object's instantiation
	}


	// set loanee name
	public void setLoaneeName()
	{
		String name;
		System.out.print("Loanee Name: ");
		name = input.nextLine();
		loaneeName = name;
	}
	
	public void setLoaneeName(String name)
	{
		loaneeName = name;
	}

	// get loanee name
	public String getLoaneeName()
	{
		return loaneeName;
	}

	// set amount loaned
	public void setAmountLoaned()
	{
		while(true){
			try{
				System.out.print("\tAmount Loaned: ");
				double amount = input.nextDouble();
				if(amount > 0 && amount <= maxLoanAmount)
					amountLoaned = amount;
				else
					throw new IllegalArgumentException(
						"Amount to loan should be > 0 and <= 10000");
				break; // correct input; break out of the while loop.
			}
			catch(InputMismatchException e){
				System.err.println("Exception: Please enter a number.");
				input.nextLine(); // discard the invalid user input
			}
			catch(IllegalArgumentException e){
				System.err.printf("Exception: %s\n", e.getMessage());
			}

			System.out.println(); // print a blank line before prompting for input again
		}
	}

	// set amount loaned
	public void setAmountLoaned(double amount)
	{
		try{
			if(amount > 0 && amount <= maxLoanAmount)
				amountLoaned = amount;
			else
				throw new IllegalArgumentException(
					"Amount to loan should be > 0 and <= 10000");
		}
		catch(InputMismatchException e){
			System.err.println("Exception: Please enter a number.");
			input.nextLine(); // discard the invalid user input
			setAmountLoaned(); // call this to get the user to input correct amount
		}
		catch(IllegalArgumentException e){
			System.err.printf("Exception: %s\n", e.getMessage());
			setAmountLoaned();
		}
	}

	// get amount loaned
	public double getAmountLoaned()
	{
		return amountLoaned;
	}

	// set months to pay off
	public void setPayOffMonths()
	{
		while(true){
			try{
				System.out.print("\tMonths to full resettlement (6, 12, 18, 24): ");
				int months = input.nextInt();
				if((months > 0 && months <= 24) && months % 6 == 0)
					payOffMonths = months;
				else
					throw new IllegalArgumentException(
						"Months in which to pay back should be "+
							"either 6, 12, 18 or 24");
				break;
			}
			catch(IllegalArgumentException e){
				System.err.printf("Exception: %s\n", e.getMessage());
			}
			catch(InputMismatchException e){
				System.err.println("Exception: Please enter an number.");
				input.nextLine(); // discard invalid input.
			}
		}
	}

	// overloaded version of setPayOffMonths
	public void setPayOffMonths(int months)
	{
		try{
			if((months > 0 && months <= 24) && months % 6 == 0)
				payOffMonths = months;
			else
				throw new IllegalArgumentException(
					"Months in which to pay back should be "+
						"either 6, 12, 18 or 24");
		}
		catch(IllegalArgumentException e){
			System.err.printf("Exception: %s\n", e.getMessage());
			setPayOffMonths(); // call the this function here after
			// an exception to ensure that the correct number of months is set.
		}
		catch(InputMismatchException e){
			System.err.println("Exception: Please enter an number.");
			input.nextLine(); // discard invalid input.
			setPayOffMonths(); // get valid payoff months.
		}
	}

	// get months in which to pay back
	public int getPayOffMonths()
	{
		return payOffMonths;
	}

	// set date loaned
	public void setDateLoaned(GregorianCalendar date)
	{
		dateLoaned = date;
	}

	public void setDateLoaned()
	{
		dateLoaned = new GregorianCalendar(); // current date.
		// this is the date set by default, by the constructor.
		// can be changed by the overloaded version of this method.
	}
	// get begin date
	public GregorianCalendar getDateLoaned()
	{
		return dateLoaned;
	}

	// set pay back by date
	public void setPayByDate()
	{
		// make a new date which is equal to the date loaned
		// then add the number of months to a full payoff to that date
		// to make it the date within which a full payoff is expected.
		payByDate = new GregorianCalendar(dateLoaned.get(dateLoaned.YEAR),
			dateLoaned.get(dateLoaned.MONTH), dateLoaned.get(dateLoaned.DAY_OF_WEEK));

		payByDate.add(payByDate.MONTH, getPayOffMonths());
	}

	// get pay back by date
	public GregorianCalendar getPayByDate()
	{
		return payByDate;
	}

	// get the fee charged based on the months that will
	// be taken to pay back, according to the fee structure
	public double getFee()
	{
		int months = getPayOffMonths();
		switch(months){
			case 6:
				return 800;
			case 12:
				return 1800;
			case 18:
				return 3000;
			case 24:
				return 4000;
		// no need for a default case here since I already
		// ensured that the months to pay back are legal
		// when I was setting them.
		}

		return -1; // this will never be executed, but the compiler
				   // requires it for successful compilation.
	}

	// return a string representation of any gregorian date
	// in a date month, year format
	public String GregDateToString(GregorianCalendar date)
	{
		String[] months =
			{"JANUARY", "FEBRUARY", "MARCH", "APRIL",
			 "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER",
			 "OCTOBER", "NOVEMBER", "DECEMBER"
			};

		return String.format("%s %s, %s",
			date.get(date.DAY_OF_WEEK), months[date.get(date.MONTH)], date.get(date.YEAR));
	}

	// convert this whole class to a string representation
	@Override
	public String toString()
	{
		return String.format(
			"%s:\t%s\n%s:\t$%,.2f\n%s:\t%s\n%s:\t%s\n%s:\t%s\n%s:\t$%,.2f",
			"Loanee Name", getLoaneeName(),
			"Amount Loaned", getAmountLoaned(),
			"Date Loaned", GregDateToString(getDateLoaned()),
			"Pay Off Months", getPayOffMonths(),
			"Pay By Date", GregDateToString(getPayByDate()),
			"Fee Charged", getFee());
	}
}