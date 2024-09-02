package com.pageobjects.HertzScreens;

import org.openqa.selenium.By;
import org.testng.Assert;

import com.framework.reusable.MobileResuableComponents;

public class LocationSearchScreen extends MobileResuableComponents {

	By locationSearchScreenTitleText = By.xpath("//android.widget.TextView[@text='Where are you picking up?']");
	By dropOffLocationSearchScreenTitleText = By.xpath("//android.widget.TextView[@text='Where does your trip end?']");
	By backNavigationButton = By.xpath(
			"//android.widget.TextView[@text='Where are you picking up?' or @text='Where does your trip end?']//preceding-sibling::android.view.View");
	By clearLocationSearchButton = By.xpath(
			"//android.widget.TextView[@text='Where are you picking up?'or @text='Where does your trip end?']/..//following-sibling::android.widget.EditText//android.view.View/android.widget.Button");
	By airportLocationText = By.xpath("//android.widget.TextView[@text='Airport locations']");
	By neighbourhoodLocationText = By.xpath("//android.widget.TextView[@text='Neighborhood locations']");
	By railLocationText = By.xpath("//android.widget.TextView[@text='Rails locations']");

	By searchLocationTxtBox = By.xpath(
			"//android.widget.TextView[@text='Where are you picking up?' or @text='Where does your trip end?']/..//following-sibling::android.widget.EditText");
	By locationAddressText = By.xpath(
			"//android.widget.TextView[@text='Airport locations' or @text='Neighborhood locations' or @text='Rails locations']/../android.view.View[1]/android.widget.TextView[2]");
	By firstlocationText = By.xpath(
			"//android.widget.TextView[@text='Airport locations' or @text='Neighborhood locations' or @text='Rails locations']/../android.view.View[1]/android.widget.TextView[1]");

	public LocationSearchScreen() {
		super();
	}

	protected void doEnterLocation(String pickUpLocation) {
		enterText(searchLocationTxtBox, pickUpLocation);
		waitUntilElementVisible(firstlocationText, 10);
	}

	protected void verifyPickUpLocationSearchScreenDisplayed() {
		Assert.assertTrue(elementExists(locationSearchScreenTitleText, 5),
				"Pick up Location search screen is not displayed");
	}

	protected void verifyDropOffLocationSearchScreenDisplayed() {
		Assert.assertTrue(elementExists(dropOffLocationSearchScreenTitleText, 5),
				"Drop Off Location search screen is not displayed");
	}

	protected void verifyAirportLocationDisplayed() {
		scrollToElementText("Airport locations");
		Assert.assertTrue(elementExists(airportLocationText, 5), "Airport Locations category is not displayed");
	}

	protected void verifyNeighbourhoodLocationsDisplayed() {
		scrollToElementText("Neighborhood locations");
		Assert.assertTrue(elementExists(neighbourhoodLocationText, 5), "Neighborhood Locations category is not displayed");
	}

	protected void verifyLocationsAreDisplayed() {
		Assert.assertTrue(elementExists(firstlocationText, 5), "Location search results is not displayed");
	}

	protected void verifyLocationsAreNotDisplayed() {
		Assert.assertFalse(elementExists(firstlocationText, 5), "Location search results is displayed");
	}

	protected void verifyRailLocationsDisplayed() {
		scrollToElementText("Rail locations");
		Assert.assertTrue(elementExists(railLocationText, 5), "Rail Locations category is not displayed");
	}

	protected void verifyLocationsAddressDisplayed() {
		Assert.assertTrue(elementExists(locationAddressText, 5), "Location address is not displayed in the result");
	}

	protected void clickClearButton() {
		clickElement(clearLocationSearchButton);
	}

	protected void verifyEnteredLocationSeacrhIsCleared() {
		Assert.assertTrue(getElementText(searchLocationTxtBox).contentEquals(""), "Location search is not cleared");
	}

	protected void clickBackNavigation() {
		clickElement(backNavigationButton);
	}

	protected void selectLocation() {
		clickElement(firstlocationText);
	}

}
