package com.cucumber.steps.HertzScreens;

import com.pageobjects.HertzScreens.ReservationConfirmationScreen;

import io.cucumber.java.en.Then;

public class ReservationConfirmationScreenSteps extends ReservationConfirmationScreen{
	
	@Then("on successful reservation confirmation screen is displayed")
	public void verify_choose_your_coverage_screen_displayed() {
		verifyConfirmationScreenDisplayed();
	}
	
	@Then("print Reservation Number")
	public void print_ReservationNumber() {
		getReservationNumber();
	}

}
