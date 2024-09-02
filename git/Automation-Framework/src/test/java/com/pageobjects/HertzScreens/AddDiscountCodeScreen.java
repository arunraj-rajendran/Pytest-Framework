package com.pageobjects.HertzScreens;

import org.openqa.selenium.By;
import org.testng.Assert;

import com.framework.reusable.MobileResuableComponents;

public class AddDiscountCodeScreen extends MobileResuableComponents {

	By discountCodeTitleText = By.xpath("//android.widget.TextView[@text='Add discount codes']");
	By discountCodeInformationLink = By.xpath("//android.widget.TextView[@text='Discount code information']");
	By CDPFieldLabelText = By.xpath("//android.widget.TextView[@text='Corporate Discount Program (CDP) / Club Code']");
	By CDPInput = By.xpath("//android.widget.TextView[@text='Corporate Discount Program (CDP) / Club Code']/following-sibling::android.widget.EditText[1]");
	By travelPurposeLabelText = By.xpath("//android.widget.TextView[@text='Purpose for booking:']");
	By leisurePurposeRadioButton = By.xpath("//android.widget.TextView[@text='Leisure']/preceding-sibling::android.widget.RadioButton[1]");
	By businessPurposeRadioButton = By.xpath("//android.widget.TextView[@text='Business']/preceding-sibling::android.widget.RadioButton[2]");
	By savedCodesLabelText = By.xpath("//android.widget.TextView[@text='Saved Codes']");
	By savedCodesDropDown = By.xpath("//android.widget.TextView[@text='Saved Codes']/following-sibling::android.view.View");
	By promotionalCouponLabelText = By.xpath("//android.widget.TextView[@text='Promotional Coupon (PC)']");
	By promotionalCouponInput = By.xpath("//android.widget.TextView[@text='Promotional Coupon (PC)']/following-sibling::android.widget.EditText[1]");
	By rateCodeLabelText = By.xpath("//android.widget.TextView[@text='Rate Code (RC)']");
	By rateCodeInput = By.xpath("//android.widget.TextView[@text='Rate Code (RC)']/following-sibling::android.widget.EditText[1]");
	By applyCTALabelText = By.xpath("//android.widget.TextView[@text='Apply']");
	By applyButton = By.xpath("//android.widget.TextView[@text='Apply']/following-sibling::android.widget.Button");
	By CDPErrorPopUpHeaderText = By.xpath("//android.widget.TextView[contains(@text,'Error')]");
	By CDPErrorPopUpContentText = By.xpath("//android.widget.TextView[contains(@text,'Corporate Discount Program (CDP) not found.')]");
	By CDPErrorPopUpOkayButton = By.xpath("//android.widget.TextView[@text='Okay']/following-sibling::android.widget.Button");
	By invalidCDPCodeFormatText = By.xpath("//android.widget.TextView[contains(@text,'Club code entered is invalid')]");
	By invalidPCCodeFormatText = By.xpath("//android.widget.TextView[contains(@text,'promotional code entered is invalid')]");
	By invalidRQCodeFormatText = By.xpath("//android.widget.TextView[contains(@text,'rate code entered is invalid')]");
	By backNavigationDiscountButton = By.xpath("//android.widget.TextView[contains(@text,'Add discount codes')]/../android.widget.Button");
	
	public AddDiscountCodeScreen() {
		super();
	}

	protected void verifyAddDiscountCodeScreenDisplayed() {
		Assert.assertTrue(elementExists(discountCodeTitleText, 40), "Add Discount Code screen is not displayed");
	}
	
	protected void verifyDiscountCodeInformationLinkDisplayed() {
		Assert.assertTrue(elementExists(discountCodeInformationLink, 40), "Discount Code Information link is not displayed in the Add discount screen");
	}
	
	protected void clickDiscountCodeInfoLink() {
		clickElement(discountCodeInformationLink);
	}
	
	protected void enterCDP(String CDPcode) {
		enterText(CDPInput, CDPcode);
	}
	
	protected void verifyInvalidCDPErrorIsDisplayed() {
		Assert.assertTrue(elementExists(invalidCDPCodeFormatText, 40), "Invalid CDP Format error is not displayed in the Add discount screen");
	}
	
	protected void verifyInvalidCDPErrorIsNotDisplayed() {
		Assert.assertFalse(elementExists(invalidCDPCodeFormatText, 2), "Invalid CDP Format error is not displayed in the Add discount screen");
	}
	
	protected void verifyNoCDPFoundErrorPopUpIsDisplayed() {
		Assert.assertTrue(elementExists(CDPErrorPopUpHeaderText, 40), "No CDP found Error popup is not displayed in the Add discount screen");
	}
	
	protected void verifyNoCDPFoundErrorPopUpContent() {
		Assert.assertTrue(elementExists(CDPErrorPopUpContentText, 40), "No CDP found Error popup content is not displayed/Created in the Add discount screen");
	}
	
	protected void clickOkayOnCDPErrorPopUp() {
		clickElement(CDPErrorPopUpOkayButton);
	}
	
	protected void verifyTravelPuposeIsDisplayed() {
		Assert.assertTrue(elementExists(travelPurposeLabelText, 40), "Travel Purpose section is not displayed in the Add discount screen");
	}
	
	protected void verifyTravelPuposeIsNotDisplayed() {
		Assert.assertFalse(elementExists(travelPurposeLabelText, 2), "Travel Purpose section is displayed in the Add discount screen though it is not required");
	}
	
	protected void verifyByDefaultBusinessIsSelected() {
		Assert.assertTrue(getAttributeValueOnElement(businessPurposeRadioButton, "checked").contentEquals("true"), "Travel Purpose Business is not selected by default in the Add discount screen");
	}
	
	protected void verifyByDefaultLeisureIsSelected() {
		Assert.assertTrue(getAttributeValueOnElement(leisurePurposeRadioButton, "checked").contentEquals("true"), "Travel Purpose Business is not selected by default in the Add discount screen");
	}
	
	protected void clickLiesure() {
		clickElement(leisurePurposeRadioButton);
	}
	
	protected void clickBusiness() {
		clickElement(businessPurposeRadioButton);
	}
	
	protected void verifySavedCDPDropDownIsDisplayed() {
		Assert.assertTrue(elementExists(savedCodesDropDown, 40), "Saved Codes dropdown is not displayed in the Add discount screen");
	}
	
	protected void selectFromSavedCDP(String CDPName) {
		By savedCodesDropDownValuesText = By.xpath("//android.widget.ScrollView/android.view.View/android.widget.TextView[@text='"+CDPName+"']");
		clickElement(savedCodesDropDownValuesText);
	}
	
	protected void enterPrmotionalCoupon(String PCCode) {
		enterText(promotionalCouponInput, PCCode);
	}
	
	protected void verifyInvalidPCErrorIsDisplayed() {
		Assert.assertTrue(elementExists(invalidPCCodeFormatText, 40), "Invalid PC Format error is not displayed in the Add discount screen");
	}
	
	protected void verifyInvalidPCErrorIsNotDisplayed() {
		Assert.assertFalse(elementExists(invalidPCCodeFormatText, 2), "Invalid PC Format error is not displayed in the Add discount screen");
	}
	
	protected void enterRateCode(String RQCode) {
		enterText(rateCodeInput, RQCode);
	}
	
	protected void verifyInvalidRQErrorIsDisplayed() {
		Assert.assertTrue(elementExists(invalidRQCodeFormatText, 40), "Invalid RQ Format error is not displayed in the Add discount screen");
	}
	
	protected void verifyInvalidRQErrorIsNotDisplayed() {
		Assert.assertFalse(elementExists(invalidRQCodeFormatText, 2), "Invalid RQ Format error is not displayed in the Add discount screen");
	}
	
	protected void clickBackNavigation() {
		clickElement(backNavigationDiscountButton);
	}
}
