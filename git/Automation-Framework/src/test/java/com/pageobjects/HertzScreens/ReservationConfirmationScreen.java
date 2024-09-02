package com.pageobjects.HertzScreens;

import org.openqa.selenium.By;
import org.testng.Assert;

import com.framework.reusable.MobileResuableComponents;

public class ReservationConfirmationScreen extends MobileResuableComponents{

	
	By confirmationScreenTitle = By.xpath("//android.widget.TextView[contains(@resource-id,'modal_topbar_header') and contains(@text,'Your Trip Summary')]");
	By reservationConfirmationNumber = By.xpath("//android.widget.TextView[contains(@text,'Confirmation Number:')]");
	
	public ReservationConfirmationScreen() {
		super();
	}
	
	protected void verifyConfirmationScreenDisplayed() {
		Assert.assertTrue(elementExists(confirmationScreenTitle, 60), "Reservation confirmation screen is not displayed");
	}
	
	protected void getReservationNumber() {
		String reservation = getElementText(reservationConfirmationNumber);
		System.out.println(reservation.replace("Confirmation Number:", ""));
	}

}
