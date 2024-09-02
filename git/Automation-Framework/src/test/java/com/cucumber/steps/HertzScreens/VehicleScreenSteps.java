package com.cucumber.steps.HertzScreens;

import com.pageobjects.HertzScreens.VehicleScreen;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;

public class VehicleScreenSteps extends VehicleScreen	{

	@Then("verify Vehicles Screen is displayed")
	public void verify_vehicle_screen_displayed() throws InterruptedException {
		verifyVehicleScreenDisplayed();
	}
	
	@When("user select vehicle {string} in the Vehicles Screen")
	public void click_on_vehicle_card(String vehicleName) {
		clickVehicleCard(vehicleName);
	}

	@Then("verify location name {string} is displayed in vehicle screen")
	public void verify_location_name_displayed(String locationName) {
		verifyLocationNameDisplayed(locationName);
	}
	
	@When("user clicks on location name in vehicle screen")
	public void click_on_location_name() {
		clickLocationDetails();
	}
	
	@Then("verify location details displayed in vehicle screen")
	public void verify_location_details_displayed() {
		verifyLocationDetailsDisplayed();
	}
	
	@Then("verify location details is not displayed in vehicle screen")
	public void verify_location_details_not_displayed() {
		verifyLocationDetailsNotDisplayed();
	}
	
	@Then("verify electric car is displayed in the top in vehicle screen")
	public void verify_electric_vehicles_in_the_top() {
		verifyFirstVehicleIsElectric();
	}
	
	@Then("verify vehicle details in the vehicle card is displayed in vehicle screen")
	public void verify_vehicle_details_in_the_card() {
		VerifyCarDetails();
	}
	
	@Then("verify per day price and est total is displayed in the vehicle card in vehicle screen")
	public void verify_perday_price_and_estTotal_is_Displayed() {
		verifyPerDayRateIsDisplayed();
		verifyEstTotalIsDisplayed();
	}
	
	@Then("verify per day price is not displayed and est total is displayed in the vehicle card in vehicle screen")
	public void verify_perday_price_and_estTotal_is_not_Displayed() {
		verifyPerDayRateIsNotDisplayed();
		verifyEstTotalIsDisplayed();
	}
	
	@Then("verify EV planner in vehicle screen")
	public void verify_EV_Planner() {
		verifyEVPlannerTextIsDisplayed();
		clickFindChargersNewarYou();
		verifyChargingStationsMapScreenDisplayed();
		verifyChargingstationsIconDisplayed();
		ClickCloseChargingStationsMapScreen();
		verifyVehicleScreenDisplayed();
	}
	
	@When("user click on back navigation in the vehicle screen")
	public void click_on_back_navigation() {
		clickBackNavigation();
	}
	
	@Then("verify recommended vehicle is available for the member in vehicle screen")
	public void  verify_recommended_vehicle_is_available() {
		verifyRecommendedVehicleDisplayed();
	}
	
}
