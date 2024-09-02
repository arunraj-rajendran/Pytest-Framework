package com.pageobjects.HertzScreens;


import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Calendar;


import org.openqa.selenium.By;
import org.testng.Assert;

import com.framework.reusable.MobileResuableComponents;

import io.appium.java_client.android.AndroidDriver;

public class HomeScreen extends MobileResuableComponents {

	By homePageWelcomeHeaderText = By.xpath("//android.view.View/android.widget.ScrollView/android.widget.TextView[1]");
	By homePageNameHeaderText = By.xpath("//android.view.View/android.widget.ScrollView/android.widget.TextView[2]");
	By homePageMemberTierText = By.xpath(
			"(//android.widget.FrameLayout[contains(@resource-id,'fragmentHolderLocation')]//android.widget.TextView[2])[1]");
	By menuIcon = By.xpath("//android.widget.ImageView[@content-desc='Menu']");
	By accountLinkText = By.xpath(
			"//androidx.appcompat.widget.LinearLayoutCompat[contains(@resource-id,'AccountLink')]/android.widget.CheckedTextView");
	By myRentalsText = By.xpath(
			"//androidx.appcompat.widget.LinearLayoutCompat[contains(@resource-id,'reservationLink')]/android.widget.CheckedTextView");
	By pickUpLocationTxtBox = By
			.xpath("//android.widget.TextView[@text='Pickup location']//following-sibling::android.widget.TextView");
	By dropoffLocationTxtBox = By
			.xpath("//android.widget.TextView[@text='Drop-off location']//following-sibling::android.widget.TextView");
	By addDifferentDropOffLocationLinkText = By
			.xpath("//android.widget.TextView[@text='Add different drop-off location']");
	By pickUpDateText = By
			.xpath("//android.widget.ScrollView/android.view.View[3]/android.view.View[1]/android.widget.TextView");
	By pickUpTimeText = By
			.xpath("//android.widget.ScrollView/android.view.View[3]//android.view.View[2]/android.widget.TextView");
	By dropOffDateText = By
			.xpath("//android.widget.ScrollView/android.view.View[4]//android.view.View[1]/android.widget.TextView");
	By dropOffTimeText = By
			.xpath("//android.widget.ScrollView/android.view.View[4]//android.view.View[2]/android.widget.TextView");
	By returnAtPickupLocationLinkText = By.xpath("//android.widget.TextView[@text='Return at pickup location']");

	By preferredCDPNameText = By.xpath("//android.widget.TextView[@text='Discount']//following-sibling::android.widget.TextView[2]");
	By travelPurposeText = By.xpath("//android.widget.TextView[@text='Discount']//following-sibling::android.widget.TextView[3]");
	By editDiscountLink = By.xpath("//android.widget.TextView[@text='Discount']//following-sibling::android.view.View/android.widget.TextView[@text='Edit']");
	By viewResultsButton = By.xpath("//android.widget.TextView[@text='View results']//following-sibling::android.widget.Button");
	By PrivacyAgreeButton = By.xpath("//android.widget.TextView[@text='I understand and agree']//following-sibling::android.widget.Button");
	
	public HomeScreen() {
		super();
	}

	protected void verifyHomeScreenDisplayed() {
		Assert.assertTrue(elementExists(homePageMemberTierText, 60), "Home Screen is not displayed after log in");
	}
	
	protected void clickIUnderstandButton() {
		if (elementExists(PrivacyAgreeButton, 5))
		clickElement(PrivacyAgreeButton);
	}

	protected void verifyTierName(String tierName) {
		Assert.assertTrue(getElementText(homePageMemberTierText).contentEquals(tierName),
				"Member tier displayed in home screen is" + getElementText(homePageMemberTierText) + " : " + tierName);
	}

	protected void doClickMenu() {
		clickElement(menuIcon);
	}

	protected void gotoAccountProfile() {
		clickElement(accountLinkText);
	}

	protected void doClickPickupLocation() {
		clickElement(pickUpLocationTxtBox);
	}

	protected void verifySelectedLocationIsPopulated(String selectedLocation) {
		Assert.assertTrue(getElementText(pickUpLocationTxtBox).contentEquals(selectedLocation),
				"Location Populated in home screen is" + getElementText(pickUpLocationTxtBox) + " : "
						+ selectedLocation);
	}

	protected void verifyAddDifferentDropOffLocationExists() {
		Assert.assertTrue(elementExists(addDifferentDropOffLocationLinkText, 5),
				"Add Different Drop Off location is not displayed after selecting pick up location");
	}

	protected void verifyAddDifferentDropOffLocationNotExists() {
		Assert.assertFalse(elementExists(addDifferentDropOffLocationLinkText, 2),
				"Add Different Drop Off location is displayed before selecting pick up location");
	}

	protected void verifySelectedDropOffLocationIsPopulated(String selectedLocation) {
		Assert.assertTrue(elementExists(dropoffLocationTxtBox, 5), "Location Populated in home screen is "
				+ getElementText(dropoffLocationTxtBox) + " : " + selectedLocation);
	}

	protected void clickDifferentDropOffLocation() {
		clickElement(addDifferentDropOffLocationLinkText);
	}

	protected void clickDropOffLocation() {
		clickElement(dropoffLocationTxtBox);
	}

	protected void verifyReturnAtPickupLocationExists() {
		Assert.assertTrue(elementExists(returnAtPickupLocationLinkText, 5),
				"Return at pick up location is not displayed for One way trip");
	}

	protected void verifyReturnAtPickupLocationNotExists() {
		Assert.assertFalse(elementExists(returnAtPickupLocationLinkText, 5),
				"Return at pick up location is displayed for Round Trip");
	}

	protected void verifyPickUpDate() throws ParseException {
		String deviceDate = ((AndroidDriver) driver).getDeviceTime("MM/DD/yyyy");
		SimpleDateFormat sdf = new SimpleDateFormat("M/d/yyyy");
		Calendar cal = Calendar.getInstance();
		try {
			cal.setTime(sdf.parse(deviceDate));
		} catch (ParseException e) {
			e.printStackTrace();
		}
		cal.add(Calendar.DATE, 14);
		String inFormat = getDateInFormat(cal);
		cal.add(Calendar.DATE, 2);
		String inFormatManagedWeekEnds = getDateInFormat(cal);
		Assert.assertTrue(
				(getElementText(pickUpDateText).contentEquals(inFormat)
						|| getElementText(pickUpDateText).contentEquals(inFormatManagedWeekEnds)),
				"Pick up date is not set to two weeks from current date - " + inFormat + "Expected :"
						+ getElementText(pickUpDateText));
	}

	protected void verifyPickUpTime() throws ParseException {
		Assert.assertTrue(getElementText(pickUpTimeText).contentEquals("12:00 PM"),
				"Pick up time is not set to 12:00 PM - " + getElementText(dropOffTimeText));
	}

	protected void verifyDropOffDate() {
		String deviceDate = ((AndroidDriver) driver).getDeviceTime("MM/DD/yyyy");
		SimpleDateFormat sdf = new SimpleDateFormat("M/d/yyyy");
		Calendar cal = Calendar.getInstance();
		try {
			cal.setTime(sdf.parse(deviceDate));
		} catch (ParseException e) {
			e.printStackTrace();
		}
		cal.add(Calendar.DATE, 16);
		String inFormat = getDateInFormat(cal);
		cal.add(Calendar.DATE, 2);
		String inFormatManagedWeekEnds = getDateInFormat(cal);
		Assert.assertTrue(
				(getElementText(dropOffDateText).contentEquals(inFormat)
						|| getElementText(dropOffDateText).contentEquals(inFormatManagedWeekEnds)),
				"Drop-off date is not set to two weeks plus two days from current date - " + inFormat + "Expected :"
						+ getElementText(dropOffDateText));
	}

	protected void verifyDropOffTime() {
		Assert.assertTrue(getElementText(dropOffTimeText).contentEquals("12:00 PM"),
				"Drop off time is not set to 12:00 PM - " + getElementText(dropOffTimeText));
	}

	private String getDateInFormat(Calendar cal) {
		SimpleDateFormat sdf = new SimpleDateFormat("M/d/yyyy");
		String dateAfter = sdf.format(cal.getTime());
		String dateAfterArr[] = dateAfter.split("/");
		return dateAfterArr[0] + "/" + dateAfterArr[1];
	}

	protected void verifyPreferredCDPName(String CDPName) {
		Assert.assertTrue(getElementText(preferredCDPNameText).contentEquals(CDPName),
				"Member tier displayed in home screen is" + getElementText(preferredCDPNameText) + " : " + CDPName);
	}
	
	protected void verifyTravelPurpose(String travelPurpose) {
		Assert.assertTrue(getElementText(travelPurposeText).contentEquals(travelPurpose),
				"Member tier displayed in home screen is" + getElementText(travelPurposeText) + " : " + travelPurpose);
	}
	
	protected void verifyEditDiscountExists() {
		Assert.assertTrue(elementExists(editDiscountLink, 40), "Edit Discount link is not displayed");
	}
	
	protected void clickViewResults() {
		clickElement(viewResultsButton);
	}
}
