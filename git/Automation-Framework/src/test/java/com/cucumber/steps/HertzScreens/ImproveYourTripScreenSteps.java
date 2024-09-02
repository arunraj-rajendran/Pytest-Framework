package com.cucumber.steps.HertzScreens;

import com.pageobjects.HertzScreens.ImproveYourTripScreen;

import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;

public class ImproveYourTripScreenSteps extends ImproveYourTripScreen{

	@Then("verify Improve Your Trip Screen is displayed")
	public void verify_improve_your_trip_screen_displayed() {
		verifyImproveYourTripScreenDisplayed();
	}
	
	@Then("verify FPO VAS card in Improve Your Trip Screen")
	public void verify_FPO_VAS_card() {
		verifyFPOVASCardDisplayed();
		verifyFPOVASCardContentDisplayed();
		verifyFPOVASCardIsIncluded();
		verifyFPOVASCardPriceIsNotDisplayed();
		verifyFPOVASAddButtonNotDisplayed();
		verifyFPOSocialProofingIsDisplayed();
		clickFPOInfo();
		verifyFPOInfoScreenIsDisplayed();
		clickFPOInfoClose();
	}
	
	@Then("verify SiriusXM VAS card in Improve Your Trip Screen")
	public void verify_siriusXM_VAS_card() {
		verifySiriusXMVASCardDisplayed();
		verifySiriusXMVASCardContentDisplayed();
		verifySiriusXMVASCardIsNotIncluded();
		verifySiriusXMVASCardPriceIsDisplayed();
		verifySiriusXMVASAddButtonIsDisplayed();
		addSiriusXM();
		verifySiriusXMVASAddedButtonIsDisplayed();
		verifySiriusXMSocialProofingIsNotDisplayed();
		clickSiriusXMInfo();
		verifySiriusXMInfoScreenIsDisplayed();
		verifyAddedButtonInforScreen();
		clickSiriusXMInfoClose();
	}
	
	@Then("verify Unlimitied Wi-Fi stay connected VAS card in Improve Your Trip Screen")
	public void verify_unlimited_WiFI_VAS_card() {
		verifyUnlimitedWiFiVASCardDisplayed();
		verifyUnlimitedWiFiVASCardContentDisplayed();
		verifyUnlimitedWiFiVASCardIsNotIncluded();
		verifyUnlimitedWiFiVASCardPriceIsDisplayed();
		verifyUnlimitedWiFiVASAddButtonIsDisplayed();
		addUnlimitedWiFi();
		verifyUnlimitedWiFiVASAddedButtonIsDisplayed();
		verifyUnlimitedWiFiSocialProofingIsNotDisplayed();
		clickUnlimitedWiFiInfo();
		verifyUnlimitedWiFiInfoScreenIsDisplayed();
		verifyAddedButtonInforScreen();
		clickUnlimitedWiFiInfoClose();
	}
	
	@Then("verify Booster Seat VAS card in Improve Your Trip Screen")
	public void verify_booster_seat_VAS_card() {
		verifyBoosterSeatVASCardDisplayed();
		verifyBoosterSeatVASCardContentDisplayed();
		verifyBoosterSeatVASCardIsNotIncluded();
		verifyBoosterSeatVASCardPriceIsDisplayed();
		verifyBoosterSeatVASAddButtonIsDisplayed();
		addBoosterSeat();
		verifyBoosterSeatVASCounterButtonIsDisplayed();
		verifyBoosterSeatSocialProofingIsNotDisplayed();
		clickBoosterSeatInfo();
		verifyBoosterSeatInfoScreenIsDisplayed();
		verifyCounterButtonInforScreen();
		clickBoosterSeatInfoClose();
	}
	
	@Then("verify Child Seat VAS card in Improve Your Trip Screen")
	public void verify_child_seat_VAS_card() {
		verifyChildSeatVASCardDisplayed();
		verifyChildSeatVASCardContentDisplayed();
		verifyChildSeatVASCardIsNotIncluded();
		verifyChildSeatVASCardPriceIsDisplayed();
		verifyChildSeatVASAddButtonIsDisplayed();
		addChildSeat();
		verifyChildSeatVASCounterButtonIsDisplayed();
		verifyChildSeatSocialProofingIsNotDisplayed();
		clickChildSeatInfo();
		verifyChildSeatInfoScreenIsDisplayed();
		verifyCounterButtonInforScreen();
		clickChildSeatInfoClose();
	}
	
	@Then("verify Infant Child Seat VAS card in Improve Your Trip Screen")
	public void verify_infant_child_seat_VAS_card() {
		verifyInfantChildSeatVASCardDisplayed();
		verifyInfantChildSeatVASCardContentDisplayed();
		verifyInfantChildSeatVASCardIsNotIncluded();
		verifyInfantChildSeatVASCardPriceIsDisplayed();
		verifyInfantChildSeatVASAddButtonIsDisplayed();
		verifyInfantChildSeatVASAddButtonIsDisabled();
		verifyInfantChildSeatSocialProofingIsNotDisplayed();
		clickInfantChildSeatInfo();
		verifyInfantChildSeatInfoScreenIsDisplayed();
		verifyAddButtonInforIsDisabled();
		clickInfantChildSeatInfoClose();
	}
	
	@Then("verify Wheel Chair VAS card in Improve Your Trip Screen")
	public void verify_wheel_chair_seat_VAS_card() {
		verifyWheelChairVASCardDisplayed();
		verifyWheelChairVASCardContentDisplayed();
		verifyWheelChairVASCardIsNotIncluded();
		verifyWheelChairVASCardPriceIsDisplayed();
		verifyWheelChairVASAddButtonIsDisplayed();
		verifyInfantChildSeatVASAddButtonIsDisabled();
		
		verifyWheelChairSocialProofingIsNotDisplayed();
		clickWheelChairInfo();
		verifyWheelChairInfoScreenIsDisplayed();
		verifyAddButtonInforIsDisabled();
		clickWheelChairInfoClose();
	}
	
	
	
	
	@When("user click on Continue button in Improve Your Trip Screen is displayed")
	public void click_on_continue() {
		clickContinue();
	}
}
