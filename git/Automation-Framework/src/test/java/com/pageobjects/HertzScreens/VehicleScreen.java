package com.pageobjects.HertzScreens;

import org.openqa.selenium.By;
import org.testng.Assert;

import com.framework.reusable.MobileResuableComponents;

public class VehicleScreen extends MobileResuableComponents {

	By vehicleScreenTitileText = By.xpath("//android.widget.TextView[@text='Vehicles']");
	By locationDetailsLinkText = By.xpath("(//android.widget.TextView[@text='Vehicles']/..//following-sibling::android.widget.TextView)[2]");
	By locationDetailsText = By.xpath("(//android.widget.TextView[@text='Vehicles']/..//following-sibling::android.widget.TextView)[2]/..//following-sibling::android.widget.ScrollView/android.widget.TextView");
	By backNavigationButton = By.xpath("//android.widget.TextView[@text='Vehicles']/../android.widget.Button");
	By perDayRateText = By.xpath("//android.widget.TextView[@text='/day']");
	By estTotalText = By.xpath("//android.widget.TextView[@text='est. total' or contains(@text,'total') or contains(@text,'Total')]");
	By evPlannerText = By.xpath("//android.widget.TextView[@text='Booking an EV?']");
	By findChargersNearYouText = By.xpath("//android.widget.TextView[contains(@text,'Find Chargers Near You')]");
	By chargingStationsMapHeaderText = By.xpath("//android.widget.TextView[@text='Charging Stations']");
	By chargingStationsIcon = By.xpath("//android.view.View[@content-desc='Google Map']/android.view.View");
	By closeChargingStationsButton = By.xpath("//android.widget.TextView[@text='Charging Stations']/../android.widget.Button");
	By electricVehicleInTheFirstCard = By.xpath("(//android.widget.TextView[@text='Vehicles']/../../android.view.View/android.view.View)[1]/android.widget.TextView[@text='Electric Vehicle']");
	By recommendedVehicleCard = By.xpath("//android.widget.TextView[@text='Recommended']");
	By EVCarDetails = By.xpath("(//android.widget.TextView[@text='Vehicles']/../../android.view.View/android.view.View)[1]//android.widget.TextView");
	By NonEVCarDetails = By.xpath("(//android.widget.TextView[@text='Vehicles']/../../android.view.View/android.view.View)[1]//android.widget.TextView");
	
	public VehicleScreen() {
		super();
	}

	protected void verifyVehicleScreenDisplayed() {
		Assert.assertTrue(elementExists(vehicleScreenTitileText, 40), "Vehicle Screen is not displayed after log in");
		Assert.assertTrue(elementExists(locationDetailsLinkText, 40), "Location details not displayed in the vehicle screen");
	}

	protected void verifyLocationNameDisplayed(String locationName) {
		Assert.assertTrue(elementExists(locationDetailsLinkText, 40), "Location details not displayed in the vehicle screen");
		Assert.assertTrue(getElementText(locationDetailsLinkText).contentEquals(locationName),
				"Location name not displayed in Vehicle screen is" + getElementText(locationDetailsLinkText) + " : " + locationName);
	}
	
	protected void verifyLocationDetailsDisplayed() {
		Assert.assertTrue(getElementCount(locationDetailsText)==3 || getElementCount(locationDetailsText)==2,
				"Location Details not displayed in Vehicle screen :"+ getElementCount(locationDetailsText));
	}
	
	protected void verifyLocationDetailsNotDisplayed() {
		Assert.assertFalse(elementExists(locationDetailsText,2),
				"Location Details displayed in Vehicle screen after collapsing");
	}
	
	protected void clickLocationDetails() {
		clickElement(locationDetailsLinkText);
	}
	
	protected void clickBackNavigation() {
		clickElement(backNavigationButton);
	}
	
	protected void clickVehicleCard(String vehicleName) {
		By vehicleCardModal = By.xpath("//android.widget.TextView[@text='"+vehicleName+"']/..");
		swipeUntilElementExists(vehicleCardModal);
		clickElement(vehicleCardModal);
	}
	
	protected void verifyPerDayRateIsDisplayed() {
		Assert.assertTrue(elementExists(perDayRateText, 40), "Per day rate is not displayed in vehicle card");
	}
	
	protected void verifyPerDayRateIsNotDisplayed() {
		Assert.assertFalse(elementExists(perDayRateText, 2), "Per day rate is displayed in vehicle card");
	}
	
	protected void verifyEstTotalIsDisplayed() {
		Assert.assertTrue(elementExists(estTotalText, 2), "Estimated total rate is not displayed in vehicle card");
	}
	
	protected void verifyEVPlannerTextIsDisplayed() {
		waitUntilElementVisible(locationDetailsLinkText, 40);
		swipeUntilElementExists(By.xpath("//android.widget.TextView[@text='Electric Vehicle']"));
		Assert.assertTrue(elementExists(evPlannerText, 2), "EV planner text is not displayed in vehicle card");
	}
	
	protected void clickFindChargersNewarYou() {
		scrollToElementText("Find Chargers Near You");
		clickElement(findChargersNearYouText);
	}
	
	protected void verifyChargingStationsMapScreenDisplayed() {
		Assert.assertTrue(elementExists(chargingStationsMapHeaderText, 40), "Charging stations map screen is not displayed");
	}
	
	
	protected void verifyChargingstationsIconDisplayed() {
		Assert.assertTrue(elementExists(chargingStationsIcon, 40), "Charging stations icon is not displayed in the map");
	}
	
	protected void ClickCloseChargingStationsMapScreen() {
		clickElement(closeChargingStationsButton);
	}

	protected void verifyFirstVehicleIsElectric() {
		Assert.assertTrue(elementExists(electricVehicleInTheFirstCard, 40), "First Vehicle is not electric vehicle/EV is not displayed for the given location");
	}
	
	protected void VerifyCarDetails() {
		if(elementExists(electricVehicleInTheFirstCard, 40)) {
			Assert.assertTrue(getElementCount(EVCarDetails)==15, "Electric Car Vehicle card is not displaying all the vehicle"+getElementCount(EVCarDetails)+":13");
			NonEVCarDetails = By.xpath("(//android.widget.TextView[@text='Vehicles']/../../android.view.View/android.view.View)[2]//android.widget.TextView");
			swipeScreen(Direction.UP);
		}
		System.out.println(getElementCount(NonEVCarDetails));
		Assert.assertTrue(getElementCount(NonEVCarDetails)==14 || getElementCount(NonEVCarDetails)==13 || getElementCount(NonEVCarDetails)==11 || getElementCount(NonEVCarDetails)==10 || getElementCount(NonEVCarDetails)==9, "Vehicle card is not displaying all the vehicle"+getElementCount(NonEVCarDetails)+":16");
	}
	
	protected void verifyRecommendedVehicleDisplayed() { 
		swipeUntilElementExists(recommendedVehicleCard);
		elementExists(recommendedVehicleCard, 5);
	}

}
