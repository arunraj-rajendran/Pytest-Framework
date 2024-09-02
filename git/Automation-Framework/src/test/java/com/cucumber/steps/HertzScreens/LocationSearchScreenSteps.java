package com.cucumber.steps.HertzScreens;

import com.pageobjects.HertzScreens.LocationSearchScreen;
import io.cucumber.java.en.When;
import io.cucumber.java.en.Then;

public class LocationSearchScreenSteps extends LocationSearchScreen {

	@Then("Location Search screen is displayed")
	public void verify_location_search_screen_displayed() {
		verifyPickUpLocationSearchScreenDisplayed();
	}

	@When("user enters the location: {string} in Location Search screen")
	public void enter_pickup_location(String location) {
		doEnterLocation(location);
	}

	@Then("verify location search results are displayed for Airport Locations, Neighborhood Locations and Rail Locaitons in Location Search screen")
	public void verify_location_search_result_displayed() {
		verifyAirportLocationDisplayed();
		verifyNeighbourhoodLocationsDisplayed();
		verifyRailLocationsDisplayed();
	}

	@Then("verify location address is displayed in Location Search screen")
	public void verify_location_address_displayed() {
		verifyLocationsAddressDisplayed();
	}

	@When("user clicks on clear location search in Location Search screen")
	public void click_clear_location_search() {
		clickClearButton();
	}

	@Then("verify the location search is cleared in Location Search screen")
	public void verify_location_search_is_cleared() {
		verifyEnteredLocationSeacrhIsCleared();
		verifyLocationsAreNotDisplayed();
	}

	@When("user clicks on back Navigation in Location Search screen")
	public void click_on_back_navigation() {
		clickBackNavigation();
	}

	@When("user selects the first location from the search result in Location Search screen")
	public void click_on_first_location() {
		selectLocation();
	}

	@Then("Drop Off Location Search screen is displayed")
	public void verify_dropoff_location_search_screen_displayed() {
		verifyDropOffLocationSearchScreenDisplayed();
	}

}
