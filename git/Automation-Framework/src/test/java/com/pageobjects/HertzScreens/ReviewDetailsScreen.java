package com.pageobjects.HertzScreens;

import org.openqa.selenium.By;
import org.testng.Assert;

import com.framework.reusable.MobileResuableComponents;

public class ReviewDetailsScreen extends MobileResuableComponents  {

	By reviewDetailsScreenTitileText = By.xpath("//android.widget.TextView[@text='Review Details']");
	By arrivalInfoText = By.xpath("//android.widget.TextView[@text='Arrival information']");
	By arrivalInfoAddEditButton = By.xpath("//android.widget.TextView[@text='Arrival information']//following-sibling::android.view.View[1]/android.widget.TextView[@text='Add' or @text='Edit']/following-sibling::android.widget.Button");
	By noArrivalInfoText = By.xpath("//android.widget.TextView[@text='No arrival details added']");
	By paymentOptionsText = By.xpath("//android.widget.TextView[@text='Payment options']");
	By rewardPointsText = By.xpath("//android.widget.TextView[contains(@text,'Rewards points: ')]");
	By noRewardPointsText = By.xpath("//android.widget.TextView[@text='You do not have enough points or this location is not accepting points.']");
	By rewardProgramText = By.xpath("//android.widget.TextView[@text='Which rewards program should we apply these rewards toward?']");
	By rewardProgramsAddEditButton = By.xpath("//android.widget.TextView[@text='Which rewards program should we apply these rewards toward?']//following-sibling::android.view.View[1]/android.widget.TextView[@text='Add' or @text='Edit']/following-sibling::android.widget.Button");
	By paymentMethodText = By.xpath("//android.widget.TextView[@text='Payment method']");
	By paymentMethodAddEditButton = By.xpath("//android.widget.TextView[@text='Payment method']//following-sibling::android.view.View[1]/android.widget.TextView[@text='Add' or @text='Edit']/following-sibling::android.widget.Button");
	By creditCardText = By.xpath("//android.widget.TextView[@text='A credit card is required to reserve this vehicle. A valid credit card must be presented at the time of rental to complete the reservation.']");
	By priceDetailsText = By.xpath("//android.widget.TextView[@text='Price Details']");
	By discountsText = By.xpath("//android.widget.TextView[@text='Discounts']");
	By rateDetailsText = By.xpath("//android.widget.TextView[@text='Rate Details']");
	By dayRateText = By.xpath("//android.widget.TextView[contains(@text,'days at')]");
	By feesSurchargesText = By.xpath("//android.widget.TextView[@text='Fees & Surcharges']");
	By feesSurchargesInfoButton = By.xpath("//android.widget.TextView[@text='Fees & Surcharges']//following-sibling::android.view.View[1]/android.widget.Button");
	By taxesText = By.xpath("//android.widget.TextView[@text='Taxes']");
	By taxesInfoButton = By.xpath("//android.widget.TextView[@text='Taxes']//following-sibling::android.view.View[1]/android.widget.Button");
	By protectionsPlansText = By.xpath("//android.widget.TextView[@text='Protection Plans']");
	By protectionsPlansInfoButton = By.xpath("//android.widget.TextView[@text='Protection Plans']//following-sibling::android.view.View[1]/android.widget.Button");
	By extrasText = By.xpath("//android.widget.TextView[@text='Extras']");
	By extrasInfoButton = By.xpath("//android.widget.TextView[@text='Extras']//following-sibling::android.view.View[1]/android.widget.Button");
	By payNowRadioButton = By.xpath("//android.widget.TextView[@text='Pay Now']//preceding-sibling::android.widget.RadioButton");
	By payLaterRadioButton = By.xpath("//android.widget.TextView[@text='Pay Later']//preceding-sibling::android.widget.RadioButton");
	By companyOrderBillingNumberText = By.xpath("//android.widget.TextView[@text='Company order/billing reference number']");
	By companyOrderBillingNumberAddEditButton = By.xpath("//android.widget.TextView[@text='Company order/billing reference number']//following-sibling::android.view.View[1]/android.widget.TextView[@text='Add' or @text='Edit']/following-sibling::android.widget.Button");
	By noCompanyOrderBillingNumberText = By.xpath("//android.widget.TextView[@text='No number added']");
	By iAgreeText = By.xpath("//android.widget.TextView[contians(@text,'I agree to the following']");
	By termsAndConditionsLink = By.xpath("//android.widget.TextView[@text='Terms and Conditions']");
	By qualificationsAndRequirementsLink = By.xpath("//android.widget.TextView[@text='Qualifications and requirements']");
	By bookNowButton = By.xpath("//android.widget.TextView[@text='Book Now']//following-sibling::android.widget.Button");
	
	public ReviewDetailsScreen() {
		super();
	}

	protected void verifyReviewDetailsScreenDisplayed() {
		Assert.assertTrue(elementExists(reviewDetailsScreenTitileText, 40,""), "Review Details screen is not displayed");
	}
	
	protected void verifyVehilceNameDisplayedInTripsummary(String carName) {
		By vehicleNameText = By.xpath("//android.widget.TextView[@text='"+carName+"']");
		Assert.assertTrue(elementExists(vehicleNameText, 40, carName), "Vehicle Name is not displayed in trip summay");
	}
	
	protected void verifyPickUpLocationTextInTripsummary(String pickUpLocation) {
		By pickUpLocationText = By.xpath("//android.widget.TextView[@text='"+pickUpLocation+"']");
		Assert.assertTrue(elementExists(pickUpLocationText, 40, pickUpLocation), "Pick up location is not displayed in trip summary");
	}
	
	protected void verifyDropOffLocationTextInTripsummary(String dropOffLocation) {
		By dropOffLocationText = By.xpath("//android.widget.TextView[@text='"+dropOffLocation+"']");
		Assert.assertTrue(elementExists(dropOffLocationText, 40, dropOffLocation), "Drop off location is not displayed in trip summary");
	}
	
	protected void verifyPickUpDateTimeTextInTripsummary(String pickUpDateTime) {
		By pickUpDateTimeText = By.xpath("//android.widget.TextView[@text='"+pickUpDateTime+"']");
		Assert.assertTrue(elementExists(pickUpDateTimeText, 40,pickUpDateTime), "Pick up Date and time is not displayed in trip summary");
	}
	
	protected void verifyDropOffDateTimeTextInTripsummary(String dropOffDateTime) {
		By dropOffDateTimeText = By.xpath("//android.widget.TextView[@text='"+dropOffDateTime+"']");
		Assert.assertTrue(elementExists(dropOffDateTimeText, 40,dropOffDateTime), "Drop OFf Date and time is not displayed in trip summary");
	}
	
	protected void verifyArrivalInfoSectionDisplayed() {
		Assert.assertTrue(elementExists(arrivalInfoText, 40,"Arrival information"), "Arrival Information section is not displayed in the review Details screen");
	}
	
	protected void verifyAddEditArrivalInfButtonDisplayed() {
		Assert.assertTrue(elementExists(arrivalInfoAddEditButton, 40, "Arrival information"), "Add/Edit Arrival Information Button is not displayed in the review Details screen");
	}
	
	protected void clickAddEditArrivalInfo() {
		clickElement(arrivalInfoAddEditButton);
	}
	
	protected void verifyNoArrivalInfoTextDisplayed() {
		Assert.assertTrue(elementExists(noArrivalInfoText, 40,"No arrival details added"), "No Arrival Information text is not displayed in the review Details screen");
	}
	
	protected void verifyNoArrivalInfoTextNotDisplayed() {
		Assert.assertFalse(elementExists(noArrivalInfoText, 3,"No arrival details added"), "No Arrival Information text is displayed in the review Details screen");
	}
	
	protected void verifypaymentOptionsTextDisplayed() {
		Assert.assertTrue(elementExists(paymentOptionsText, 40,"Payment options"), "Payment option is not displayed in the review Details screen");
	}
	
	protected void verifyRewardPointsDisplayed() {
		Assert.assertTrue(elementExists(rewardPointsText, 40,"Rewards points: "), "Reward points text is not displayed in the review Details screen");
	}
	
	protected void verifyNoRewardPointsTextDisplayed() {
		Assert.assertTrue(elementExists(noRewardPointsText, 40,"enough points"), "'You do not have enough points or this location is not accepting points.' is not displayed in the review Details screen");
	}
	
	protected void verifyRewardsProgramDisplayed() {
		Assert.assertTrue(elementExists(rewardProgramText, 40,"rewards program"), "Reward Program section is not displayed in the review Details screen");
	}
	
	protected void clickAddEditRewardPrograms() {
		clickElement(rewardProgramsAddEditButton);
	}
	
	protected void verifyRewardsProgramNameDisplayed(String rewardProgramName) {
		By rewardProgramNameText = By.xpath("//android.widget.TextView[@text='"+rewardProgramName+"']");
		Assert.assertTrue(elementExists(rewardProgramNameText, 40, rewardProgramName), "Reward program name is not displayed in the review Details screen");
	}
	
	protected void verifyPaymentMethodDisplayed() {
		Assert.assertTrue(elementExists(paymentMethodText, 40,"Payment method"), "Payment Method section is not displayed in the review Details screen");
	}
	
	protected void clickAddEditPaymentMethod() {
		clickElement(paymentMethodAddEditButton);
	}
	
	protected void verifyCreditCardNumberDisplayed(String cardNumber) {
		By creditCardNumberText = By.xpath("//android.widget.TextView[@text='"+cardNumber.substring(cardNumber.length()-4)+"']");
		Assert.assertTrue(elementExists(creditCardNumberText, 40, cardNumber.substring(cardNumber.length()-4)), "Credit card Number is not displayed in the review Details screen");
	}
	
	protected void verifyCreditCardTextDisplayed() {
		Assert.assertTrue(elementExists(creditCardText, 40, "A credit card is required"), "Credit card text is not displayed in the review Details screen");
	}
	
	protected void verifyPriceDetailsDisplayed() {
		Assert.assertTrue(elementExists(priceDetailsText, 40,"Price Details"), "Price Details section is not displayed in the review Details screen");
	}
	
	protected void verifyDiscountsUnderPricingDisplayed() {
		Assert.assertTrue(elementExists(discountsText, 40, "Discounts"), "Discounts under pricing section is not displayed in the review Details screen");
	}
	
	protected void verifyDiscountCodeTextDisplayed(String discountCode) {
		By discountCodeText = By.xpath("//android.widget.TextView[@text='"+discountCode+"']");
		Assert.assertTrue(elementExists(discountCodeText, 40,"Discounts"), "Applied Discounts code name under pricing section is not displayed in the review Details screen");
	}
	
	protected void verifyRateDetailsDisplayed() {
		Assert.assertTrue(elementExists(rateDetailsText, 40,"Rate Details"), "Rate Details under pricing section is not displayed in the review Details screen");
	}
	
	protected void verifyPerDayRateDetailsDisplayed() {
		Assert.assertTrue(elementExists(dayRateText, 40,"days at"), "Rate per days under pricing section is not displayed in the review Details screen");
	}
	
	protected void verifyFeeAndSurchargeDisplayed() {
		Assert.assertTrue(elementExists(feesSurchargesText, 40,"Fees & Surcharges"), "Fee and Surcharges under pricing section is not displayed in the review Details screen");
	}
	
	protected void clickFeeAndSurchargeInfo() {
		clickElement(feesSurchargesInfoButton);
	}
	
	protected void verifyTaxesDisplayed() {
		Assert.assertTrue(elementExists(feesSurchargesText, 40,"Taxes"), "Taxes under pricing section is not displayed in the review Details screen");
	}
	
	protected void clickTaxesInfo() {
		clickElement(taxesInfoButton);
	}
	
	protected void verifyProtectionPlansDisplayed() {
		Assert.assertTrue(elementExists(protectionsPlansText, 40,"Protection Plans"), "Protection Plans under pricing section is not displayed in the review Details screen");
	}
	
	protected void clickProtectionPlansInfo() {
		clickElement(protectionsPlansInfoButton);
	}
	
	protected void verifyExtrasDisplayed() {
		Assert.assertTrue(elementExists(extrasText, 40,"Extras"), "Extras under pricing section is not displayed in the review Details screen");
	}
	
	protected void clickExtrasInfo() {
		clickElement(extrasInfoButton);
	}
	
	protected void clickPayNow() {
		clickElement(payNowRadioButton);
	}
	
	protected void clickPayLater() {
		clickElement(payNowRadioButton);
	}
	
	protected void verifyPayNowDisplayed() {
		Assert.assertTrue(elementExists(payNowRadioButton, 40,"Pay Now"), "Pay Now is not displayed in the review Details screen");
	}
	
	protected void verifyPayLaterDisplayed() {
		Assert.assertTrue(elementExists(payLaterRadioButton, 40,"Pay Later"), "Pay Later is not displayed in the review Details screen");
	}
	
	protected void verifyCompanyBillingNumberDisplayed() {
		Assert.assertTrue(elementExists(companyOrderBillingNumberText, 40,"Company order"), "Company or Billing order number is not displayed in the review Details screen");
	}
	
	protected void clickAddEditCompanyBillingNumber() {
		clickElement(companyOrderBillingNumberAddEditButton);
	}
	
	protected void verifyNoCompanyBillingNumberDisplayed() {
		Assert.assertTrue(elementExists(noCompanyOrderBillingNumberText, 40,"No number added"), "'No number added' text under Company or Billing order number is not displayed in the review Details screen");
	}
	
	protected void verifyIAgreeTextDisplayed() {
		Assert.assertTrue(elementExists(iAgreeText, 40, "I agree to the following"), "'I Agree to the following' is not displayed in the review Details screen");
	}
	
	protected void verifyTermsAndConditonsDisplayed() {
		Assert.assertTrue(elementExists(termsAndConditionsLink, 40,"Terms and Conditions"), "Terms and Conditions Link is not displayed in the review Details screen");
	}
	
	protected void verifyTermsAndConditonsNotDisplayed() {
		Assert.assertFalse(elementExists(termsAndConditionsLink, 3,"Terms and Conditions"), "Terms and Conditions Link is displayed in the review Details screen");
	}
	
	protected void clickTermsAndConditions() {
		clickElement(termsAndConditionsLink);
	}
	
	protected void verifyQualificationAndRequirementsDisplayed() {
		Assert.assertTrue(elementExists(qualificationsAndRequirementsLink, 40,"Qualifications and requirements"), "Qualification and Requirements Link is not displayed in the review Details screen");
	}
	
	protected void verifyQualificationAndRequirementsNotDisplayed() {
		Assert.assertFalse(elementExists(qualificationsAndRequirementsLink, 3,"Qualifications and requirements"), "Qualification and Requirements Link is displayed in the review Details screen");
	}
	
	protected void clickQualificationAndRequirements() {
		clickElement(qualificationsAndRequirementsLink);
	}
	
	protected void clickBookNow() {
		clickElement(bookNowButton);
	}
}
