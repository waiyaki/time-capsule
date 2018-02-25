/*
 * The file DemoLoan.java
 * Contains a class DemoLoan that tests the functionality
 * of both Loan and AnnualLoan classes.
*/

import java.util.Scanner;

public class DemoLoan
{
	public static void main(String[] args)
	{
		String loaneeOne, loaneeTwo;
		String loanee3, loanee4;

		// get loanee names
		loaneeOne = getLoaneeName();
		loaneeTwo = getLoaneeName();
		loanee3 = getLoaneeName();
		loanee4 = getLoaneeName();

		System.out.println();

		// make annual loan objects

		// annual loanees, payoff time has to be 12 months.
		AnnualLoan annualLoaneeOne = new AnnualLoan(loaneeOne, 10000, 12);
		AnnualLoan annualLoaneeTwo = new AnnualLoan(loaneeTwo);

		// make loan objects

		// general loanees, payoff time can be any duration specified
		// in the fee structure
		Loan genLoaneeOne = new Loan(loanee3);
		Loan genLoaneeTwo = new Loan(loanee4, 5690, 18);

		// output the loan objects to the console
		// annual loanees. Implicitly call the objects toString() methods.
		System.out.printf("%s\n\n%s\n\n", annualLoaneeOne, annualLoaneeTwo);

		// general loanee
		System.out.printf("%s\n\n%s\n\n", genLoaneeOne, genLoaneeTwo);
	}

	public static String getLoaneeName()
	{
		Scanner input = new Scanner(System.in);
		System.out.print("Enter Loanee's Name: ");
		String name = input.nextLine();

		return name;
	}
}