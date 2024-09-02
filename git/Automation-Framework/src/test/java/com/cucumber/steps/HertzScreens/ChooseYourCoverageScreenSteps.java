package com.cucumber.steps.HertzScreens;

import com.pageobjects.HertzScreens.ChooseYourCoveragesScreen;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;

public class ChooseYourCoverageScreenSteps extends ChooseYourCoveragesScreen	{
	@Then("verify Choose Your Coverage Screen is displayed")
	public void verify_choose_your_coverage_screen_displayed() {
		verifyChooseYourCoverageScreenDisplayed();
		verifyChooseYourCoverageScreenDisplayed();
	}
	
	@When("user click on Continue button in Choose Your Coverage Screen")
	public void click_on_continue() {
		clickContinue();
	}
	
	@Then("verify Protect the car title, short description and included is displayed in choose your coverage screen")
	public void verify_protect_the_car_vascard() {
		verifyProtectYourCarVASCardDisplayed();
		verifyProtectYourCarVASCardContentDisplayed();
		verifyProtectYourCarVASCardIsIncluded();
		verifyProtectYourCarVASCardPriceIsNotDisplayed();
		verifyProtectYourCarVASAddButtonNotDisplayed();
	}
	
	@Then("verify social proofing is displayed for protect the car in choose your coverage screen")
	public void verify_social_proofing_protect_the_car() {
		verifyProtectYourCarSocialProofingIsDisplayed();
	}
	
	@Then("verify info screen is displayed for Protect the car")
	public void verify_info_Screen_protect_the_car() {
		clickProtectYourCarInfo();
		verifyProtectTheCarInfoScreenIsDisplayed();
		clickProtectTheCarInfoClose();
	}

	@Then("verify Liability Protection title, short description is displayed and included is not displayed in choose your coverage screen")
	public void verify_liability_protection_vascard() {
		verifyLiabilityProtectionVASCardDisplayed();
		verifyLiabilityProtectionVASCardContentDisplayed();
		verifyLiabilityProtectionVASCardIsNotIncluded();
		verifyLiabilityProtectionVASCardPriceIsDisplayed();
		verifyLiabilityProtectionVASAddButtonIsDisplayed();
		addLiabilityProtection();
		verifyLiabilityProtectionVASAddedButtonIsDisplayed();
	}
	
	@Then("verify social proofing is displayed for Liability Protection in choose your coverage screen")
	public void verify_social_proofing_liability_protection() {
		verifyLiabilityProtectionSocialProofingIsDisplayed();
	}
	
	@Then("verify info screen is displayed for Liability Protection")
	public void verify_info_Screen_liability_protection() {
		clickLiabilityProtectionInfo();
		verifyLiabilityProtectionInfoScreenIsDisplayed();
		clickLiabilityProtectionInfoClose();
	}
	
	@Then("verify Personal Protection Package title, short description and included is displayed in choose your coverage screen")
	public void verify_personal_protection_package_vascard() {
		verifyPersonalProtectionPackageVASCardDisplayed();
		verifyPersonalProtectionPackageVASCardContentDisplayed();
		verifyPersonalProtectionPackageVASCardIsIncluded();
		verifyPersonalProtectionPackageVASCardPriceIsNotDisplayed();
		verifyPersonalProtectionPackageVASAddButtonNotDisplayed();
	}
	
	@Then("verify social proofing is displayed for Personal Protection Package  in choose your coverage screen")
	public void verify_social_proofing_personal_protection_package() {
		verifyPersonalProtectionPackageSocialProofingIsDisplayed();
	}
	
	@Then("verify info screen is displayed with add button for Personal Protecion Package")
	public void verify_info_Screen_personal_protection_package() {
		clickPersonalProtectionPackageInfo();
		verifyPersonalProtectionPackageInfoScreenIsDisplayed();
		clickPersonalProtectionPackageInfoClose();
	}

	@Then("verify Drive with total peace of mind title, short description is displayed and included is not displayed in choose your coverage screen")
	public void verify_drive_with_total_peace_of_mind_vascard() {
		verifyDriveWithTotalPeaceOfMindVASCardDisplayed();
		verifyDriveWithTotalPeaceOfMindVASCardContentDisplayed();
		verifyDriveWithTotalPeaceOfMindVASCardIsNotIncluded();
		verifyDriveWithTotalPeaceOfMindVASCardPriceIsDisplayed();
		verifyDriveWithTotalPeaceOfMindVASAddButtonIsDisplayed();
		addDriveWithTotalPeaceOfMind();
		verifyDriveWithTotalPeaceOfMindVASAddedButtonIsDisplayed();
	}
	
	@Then("verify social proofing is not displayed for Drive with total peace of mind in choose your coverage screen")
	public void verify_social_proofing_drive_with_total_peace_of_mind() {
		verifyDriveWithTotalPeaceOfMindSocialProofingIsNotDisplayed();
	}
	
	@Then("verify info screen is displayed with added button if Drive with peace of mind is added in choose your coverage screen")
	public void verify_info_Screen_drive_with_total_peace_of_mind() {
		clickDriveWithTotalPeaceOfMindInfo();
		verifyDriveWithTotalPeaceOfMindInfoScreenIsDisplayed();
		verifyAddedButtonExists();
		clickDriveWithTotalPeaceOfMindInfoClose();
	}
	
	@Then("verify Loss Damage Waiver title, short description is displayed in choose your coverage screen")
	public void verify_loss_damage_waiver_vascard() {
		verifyLossDamageWaiverVASCardDisplayed();
		verifyLossDamageWaiverVASCardContentDisplayed();
		verifyLossDamageWaiverVASCardPriceIsDisplayed();
		verifyLossDamageWaiverVASAddButtonIsDisplayed();
		addlossDamageWaiver();
	}
	 
	@Then("verify social proofing is not displayed for Loss Damage Waiver in choose your coverage screen")
	public void verify_social_proofing_loss_damage_waiver() {
		verifyLossDamageWaiverSocialProofingIsNotDisplayed();
	}
	
	@Then("verify info screen is displayed for Loss Damage Waiver")
	public void verify_info_Screen_loss_damage_waiver() {
		clickLossDamageWaiverInfo();
		verifyLossDamageWaiverInfoScreenIsDisplayed();
		clickAddedButtonInfo();
		clickLossDamageWaiverInfoClose();
	}
	
	@Then("verify continue button is disabled when no VAS is selected")
	public void verify_continue_button_is_disabled() {
		verifyContinueButtonIsDisabled();
	}
	
	@Then("verify continue without proptection card and its info screen")
	public void verify_continue_without_protection_vascard() {
		verifyContinueButtonIsDisabled();
		verifyContinueWithoutProtectionCardDisplayed();
		verifyContinueWithoutProtectionCardContentDisplayed();
		clickContinueWithoutProtectionInfo();
		verifyContinueWithoutProtectionInfoScreenIsDisplayed();
		clickContinueWithoutProtectionInfoClose();
		clickContinueWithoutProtectionCheckBox();
		verifyContinueButtonIsEnabled();
	}
	
	@When("user add Liability Protection in choose your coverage screen")
	public void add_liability_protection() {
		addLiabilityProtection();
	}

}
