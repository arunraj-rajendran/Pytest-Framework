package com.cucumber.steps.HertzScreens;

import java.text.ParseException;

import com.pageobjects.HertzScreens.HomeScreen;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;

public class HomeScreenSteps extends HomeScreen {

	@Then("verify Home screen is displayed")
	public void verify_home_screen_displayed() {
		clickIUnderstandButton();
		verifyHomeScreenDisplayed();
	}

	@Then("verify Member tier displayed is same as: {string} in Home screen")
	public void verify_member_tier_displayed(String memberTier) {
		verifyTierName(memberTier);
	}

	@When("user clicks on Menu icon in Home screen")
	public void click_on_menu() {
		doClickMenu();
	}

	@When("user clicks on Account Summary link from navigation menu in Home screen")
	public void goto_account_summary() {
		gotoAccountProfile();
	}

	@When("user clicks on Pick up location input field in Home screen")
	public void click_on_pickup_location() {
		doClickPickupLocation();
	}

	@Then("verify location: {string} is populated in Pick up location field in Home screen")
	public void verify_location_is_populated(String selectedLocation) {
		verifySelectedLocationIsPopulated(selectedLocation);
	}

	@Then("verify location: {string} is populated in Drop off location field in Home screen")
	public void verify_dropff_location_is_populated(String selectedLocation) {
		verifySelectedDropOffLocationIsPopulated(selectedLocation);
	}

	@When("user clicks on Drop Off location input field in Home screen")
	public void click_on_dropoff_location() {
		clickDropOffLocation();
	}

	@Then("verify Add Different Drop off location link is displayed in Home screen")
	public void verify_add_different_dropoff_location_is_displayed() {
		verifyAddDifferentDropOffLocationExists();
	}

	@Then("verify Add Different Drop off location link is not displayed in Home screen")
	public void verify_add_different_dropoff_location_is_not_displayed() {
		verifyAddDifferentDropOffLocationNotExists();
	}

	@When("user clicks on Add Different Drop Off location link in Home screen")
	public void click_on_add_different_dropoff_location() {
		clickDifferentDropOffLocation();
	}

	@Then("verify Return at pickup location link is displayed in Home screen")
	public void verif_return_at_pickup_location_displayed() {
		verifyReturnAtPickupLocationExists();
	}

	@Then("verify Return at pickup location link is not displayed in Home screen")
	public void verify_return_at_pickup_location_not_displayed() {
		verifyReturnAtPickupLocationNotExists();
	}
	
	@Then("verify Pick up date is set two weeks from today in Home screen")
	public void verify_pickup_date_is_two_weeks_from_today() throws ParseException {
		verifyPickUpDate();
	}
	
	@Then("verify Pick up time is set to 12:00 PM in Home screen")
	public void verify_pickup_time_is_12PM() throws ParseException {
		verifyPickUpTime();
	}
	
	@Then("verify drop-off date is set two weeks plus two days from today in Home screen")
	public void verify_dropoff_date_is_two_weeks_from_today() throws ParseException {
		verifyDropOffDate();
	}
	
	@Then("verify drop-off time is set to 12:00 PM in Home screen")
	public void verify_dropoff_time_is_12PM() throws ParseException {
		verifyDropOffTime();
	}
	
	@When("user clicks on the View Results button in the Home Screen")
	public void click_on_view_results() {
		clickViewResults();
	}
}
