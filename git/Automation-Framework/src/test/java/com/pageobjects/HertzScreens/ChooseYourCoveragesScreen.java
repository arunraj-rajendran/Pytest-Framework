package com.pageobjects.HertzScreens;

import org.openqa.selenium.By;
import org.testng.Assert;

import com.framework.reusable.MobileResuableComponents;

public class ChooseYourCoveragesScreen extends MobileResuableComponents {

	By chooseYourCoverageScreenTitleText = By.xpath("//android.widget.TextView[@text='Choose your coverage(s)']");
	By chooseYourCoverageScreenSubTitleText = By.xpath("//android.widget.TextView[@text='Let’s Get You Protected']");
	
	By protectTheCarVASCardText = By.xpath("//android.widget.TextView[@text='Protect the car']");
	By protectTheCarVASContentText = By.xpath("//android.widget.TextView[@text='Protect the car']/following-sibling::android.widget.TextView[contains(@text,'Rental Vehicle Damage')]");
	By protectTheCarIncludedText = By.xpath("//android.widget.TextView[@text='Protect the car']/following-sibling::android.widget.TextView[@text='Included']");
	By protectTheCarPriceText = By.xpath("//android.widget.TextView[@text='Protect the car']/following-sibling::android.widget.TextView[contains(@text,'/day')]");
	By protectTheCarAddButton = By.xpath("//android.widget.TextView[@text='Protect the car']/following-sibling::android.view.View/android.widget.TextView[@text='Add']/../android.widget.Button");
	By protectTheCarAddedButton = By.xpath("//android.widget.TextView[@text='Protect the car']/following-sibling::android.view.View/android.widget.TextView[@text='Added']/../android.widget.Button");
	By protectTheCarSocialProofingText = By.xpath("//android.widget.TextView[@text='Protect the car']/following-sibling::android.widget.TextView[contains(@text,'added last month')]");
	By protectTheCarInfoLink = By.xpath("//android.widget.TextView[@text='Protect the car']/../following-sibling::android.view.View[1]/android.widget.Button");
	By protectTheCarInfoScreenText = By.xpath("//android.widget.TextView[@text='Protect the car']");
	By protectTheCarInfoCloseButton = By.xpath("//android.widget.TextView[@text='Protect the car']/following-sibling::android.widget.Button");
	
	By liabilityProtectionVASCardText = By.xpath("//android.widget.TextView[@text='Liability Protection']");
	By liabilityProtectionVASContentText = By.xpath("//android.widget.TextView[@text='Liability Protection']/following-sibling::android.widget.TextView[contains(@text,'Injury/property damage to others')]");
	By liabilityProtectionIncludedText = By.xpath("//android.widget.TextView[@text='Liability Protection']/following-sibling::android.widget.TextView[@text='Included']");
	By liabilityProtectionPriceText = By.xpath("//android.widget.TextView[@text='Liability Protection']/following-sibling::android.widget.TextView[contains(@text,'/day')]");
	By liabilityProtectionAddButton = By.xpath("//android.widget.TextView[@text='Liability Protection']/following-sibling::android.view.View/android.widget.TextView[@text='Add']/../android.widget.Button");
	By liabilityProtectionAddedButton = By.xpath("//android.widget.TextView[@text='Liability Protection']/following-sibling::android.view.View/android.widget.TextView[@text='Added']/../android.widget.Button");
	By liabilityProtectionSocialProofingText = By.xpath("//android.widget.TextView[@text='Liability Protection']/following-sibling::android.widget.TextView[contains(@text,'added last month')]");
	By liabilityProtectionInfoLink = By.xpath("//android.widget.TextView[@text='Liability Protection']/../following-sibling::android.view.View[1]/android.widget.Button");
	By liabilityProtectionInfoScreenText = By.xpath("//android.widget.TextView[@text='Liability Protection']");
	By liabilityProtectionInfoCloseButton = By.xpath("//android.widget.TextView[@text='Liability Protection']/following-sibling::android.widget.Button");
	
	By personalProtectionPackageVASCardText = By.xpath("//android.widget.TextView[@text='Personal Protection Package']");
	By personalProtectionPackageVASContentText = By.xpath("//android.widget.TextView[@text='Personal Protection Package']/following-sibling::android.widget.TextView[contains(@text,'Accidental injury/death or theft')]");
	By personalProtectionPackageIncludedText = By.xpath("//android.widget.TextView[@text='Personal Protection Package']/following-sibling::android.widget.TextView[@text='Included']");
	By personalProtectionPackagePriceText = By.xpath("//android.widget.TextView[@text='Personal Protection Package']/following-sibling::android.widget.TextView[contains(@text,'/day')]");
	By personalProtectionPackageAddButton = By.xpath("//android.widget.TextView[@text='Personal Protection Package']/following-sibling::android.view.View/android.widget.TextView[@text='Add']/../android.widget.Button");
	By personalProtectionPackageAddedButton = By.xpath("//android.widget.TextView[@text='Personal Protection Package']/following-sibling::android.view.View/android.widget.TextView[@text='Added']/../android.widget.Button");
	By personalProtectionPackageSocialProofingText = By.xpath("//android.widget.TextView[@text='Personal Protection Package']/following-sibling::android.widget.TextView[contains(@text,'added last month')]");
	By personalProtectionPackageInfoLink = By.xpath("//android.widget.TextView[@text='Personal Protection Package']/../following-sibling::android.view.View[1]/android.widget.Button");
	By personalProtectionPackageInfoScreenText = By.xpath("//android.widget.TextView[@text='Personal Protection Package']");
	By personalProtectionPackageInfoCloseButton = By.xpath("//android.widget.TextView[@text='Personal Protection Package']/following-sibling::android.widget.Button");
	
	
	By driveWithTotalPeaceOfMindVASCardText = By.xpath("//android.widget.TextView[@text='Drive with total peace of mind']");
	By driveWithTotalPeaceOfMindVASContentText = By.xpath("//android.widget.TextView[@text='Drive with total peace of mind']/following-sibling::android.widget.TextView[contains(@text,'Reduce your financial liability for non-mechanical')]");
	By driveWithTotalPeaceOfMindIncludedText = By.xpath("//android.widget.TextView[@text='Drive with total peace of mind']/following-sibling::android.widget.TextView[@text='Included']");	
	By driveWithTotalPeaceOfMindPriceText = By.xpath("//android.widget.TextView[@text='Drive with total peace of mind']/following-sibling::android.widget.TextView[contains(@text,'/day')]");
	By driveWithTotalPeaceOfMindAddButton = By.xpath("//android.widget.TextView[@text='Drive with total peace of mind']/following-sibling::android.view.View/android.widget.TextView[@text='Add']/../android.widget.Button");
	By driveWithTotalPeaceOfMindAddedButton = By.xpath("//android.widget.TextView[@text='Drive with total peace of mind']/following-sibling::android.view.View/android.widget.TextView[@text='Added']/../android.widget.Button");
	By driveWithTotalPeaceOfMindSocialProofingText = By.xpath("//android.widget.TextView[@text='Drive with total peace of mind']/following-sibling::android.widget.TextView[contains(@text,'added last month')]");
	By driveWithTotalPeaceOfMindInfoLink = By.xpath("//android.widget.TextView[@text='Drive with total peace of mind']/../following-sibling::android.view.View[1]/android.widget.Button");
	By driveWithTotalPeaceOfMindInfoScreenText = By.xpath("//android.widget.TextView[@text='Drive with total peace of mind']");
	By driveWithTotalPeaceOfMindInfoCloseButton = By.xpath("//android.widget.TextView[@text='Drive with total peace of mind']/following-sibling::android.widget.Button");
	
	
	By lossDamageWaiverVASCardText = By.xpath("//android.widget.TextView[@text='Loss Damage Waiver']");
	By lossDamageWaiverVASContentText = By.xpath("//android.widget.TextView[@text='Loss Damage Waiver']/following-sibling::android.widget.TextView[contains(@text,'Get Added Peace of Mind')]");
	By lossDamageWaiverIncludedText = By.xpath("//android.widget.TextView[@text='Loss Damage Waiver']/following-sibling::android.widget.TextView[@text='Included']");	
	By lossDamageWaiverPriceText = By.xpath("//android.widget.TextView[@text='Loss Damage Waiver']/following-sibling::android.widget.TextView[contains(@text,'/day')]");
	By lossDamageWaiverAddButton = By.xpath("//android.widget.TextView[@text='Loss Damage Waiver']/following-sibling::android.view.View/android.widget.TextView[@text='Add']/../android.widget.Button");
	By lossDamageWaiverAddedButton = By.xpath("//android.widget.TextView[@text='Loss Damage Waiver']/following-sibling::android.view.View/android.widget.TextView[@text='Added']/../android.widget.Button");
	By lossDamageWaiverSocialProofingText = By.xpath("//android.widget.TextView[@text='Loss Damage Waiver']/following-sibling::android.widget.TextView[contains(@text,'added last month')]");
	By lossDamageWaiverInfoLink = By.xpath("//android.widget.TextView[@text='Loss Damage Waiver']/../following-sibling::android.view.View[1]/android.widget.Button");
	By lossDamageWaiverInfoScreenText = By.xpath("//android.widget.TextView[@text='Loss Damage Waiver']");
	By lossDamageWaiverInfoCloseButton = By.xpath("//android.widget.TextView[@text='Loss Damage Waiver']/following-sibling::android.widget.Button");
	
	
	By continueWithoutProtectionCardText = By.xpath("//android.widget.TextView[@text='Continue Without Protection']");
	By continueWithoutProtectionContentText = By.xpath("//android.widget.TextView[@text='Continue Without Protection']/following-sibling::android.widget.TextView[contains(@text,'Your personal insurance or credit card may not fully cover this trip.')]");
	By continueWithoutProtectionCheckbox = By.xpath("//android.widget.TextView[@text='Continue Without Protection']/following-sibling::android.view.View/android.view.View");
	By continueWithoutProtectionInfoLink = By.xpath("//android.widget.TextView[@text='Continue Without Protection']/../following-sibling::android.view.View[1]/android.widget.Button");
	By continueWithoutProtectionInfoScreenText = By.xpath("//android.widget.TextView[contains(@text,'Ensure You')]");
	By continueWithoutProtectionInfoCloseButton = By.xpath("//android.widget.TextView[contains(@text,'Ensure')]/following-sibling::android.widget.Button");
	
	By addForButtonInfoScreenButton = By.xpath("//android.widget.TextView[contains(@text,'Add for')]/following-sibling::android.widget.Button");
	By addedButtonInfoScreenButton = By.xpath("//android.widget.TextView[contains(@text,'Added')]/following-sibling::android.widget.Button");
	By continueButton = By.xpath("//android.widget.TextView[@text='Continue']/following-sibling::android.widget.Button");
	By parentOfcontinueButton = By.xpath("//android.widget.TextView[@text='Continue']/following-sibling::android.widget.Button/..");
	
	public ChooseYourCoveragesScreen() {
		super();
	}
	
	protected void verifyChooseYourCoverageScreenDisplayed() {
		Assert.assertTrue(elementExists(chooseYourCoverageScreenTitleText, 40), "Choose your coverage screen is not displayed");
	}
	
	protected void verifyChooseYourCoverageScreenSubtitleDisplayed() {
		Assert.assertTrue(elementExists(chooseYourCoverageScreenSubTitleText, 40), "Choose your coverage screen sub title 'Let’s Get You Protected' is not displayed");
	}
	
	protected void verifyProtectYourCarVASCardDisplayed() {
		Assert.assertTrue(elementExists(protectTheCarVASCardText, 40), "Protect your car VAS card is not correct/displayed");
	}
	
	protected void verifyProtectYourCarVASCardContentDisplayed() {
		Assert.assertTrue(elementExists(protectTheCarVASContentText, 40), "protect your car VAS card content is not correct/Displayed");
	}
	
	protected void verifyProtectYourCarVASCardIsIncluded() {
		Assert.assertTrue(elementExists(protectTheCarIncludedText, 40), "Protect your car VAS card is not included from account profile");
	}
	
	protected void verifyProtectYourCarVASCardIsNotIncluded() {
		Assert.assertFalse(elementExists(protectTheCarIncludedText, 2), "Protect your car VAS card is included from account profile though it is not expected");
	}
	
	protected void verifyProtectYourCarVASCardPriceIsDisplayed() {
		Assert.assertTrue(elementExists(protectTheCarPriceText, 40), "Protect your car price details is not displayed");
	}
	
	protected void verifyProtectYourCarVASCardPriceIsNotDisplayed() {
		Assert.assertFalse(elementExists(protectTheCarPriceText, 2), "Protect your car price is displayed even after it is added/included");
	}
	
	protected void verifyProtectYourCarVASAddButtonIsDisplayed() {
		Assert.assertTrue(elementExists(protectTheCarAddButton, 40), "Protect your car Add button is not displayed");
	}
	
	protected void verifyProtectYourCarVASAddedButtonIsDisplayed() {
		Assert.assertTrue(elementExists(protectTheCarAddedButton, 40), "Protect your car Add button is not displayed");
	}
	
	protected void verifyProtectYourCarVASAddButtonNotDisplayed() {
		Assert.assertFalse(elementExists(protectTheCarAddButton, 2), "Protect your car Add button is displayed even after it is added/included");
	}
	
	protected void addProtectTheCar() {
		clickElement(protectTheCarVASCardText);;
	}
	
	protected void verifyProtectYourCarSocialProofingIsDisplayed() {
		Assert.assertTrue(elementExists(protectTheCarSocialProofingText, 40), "Protect your car Add button is not displayed");
	}
	
	protected void clickProtectYourCarInfo() {
		clickElement(protectTheCarInfoLink);;
	}
	
	protected void verifyProtectTheCarInfoScreenIsDisplayed() {
		Assert.assertTrue(getElementCount(protectTheCarInfoScreenText)==2, "Protect the car info screen is not displayed");
	}
	
	protected void clickProtectTheCarInfoClose() {
		clickElement(protectTheCarInfoCloseButton);;
	}
	
	
	protected void verifyLiabilityProtectionVASCardDisplayed() {
		Assert.assertTrue(elementExists(liabilityProtectionVASCardText, 40), "Liability Protection VAS card is not correct/displayed");
	}
	
	protected void verifyLiabilityProtectionVASCardContentDisplayed() {
		Assert.assertTrue(elementExists(liabilityProtectionVASContentText, 40), "Liability Protection VAS card content is not correct/Displayed");
	}
	
	protected void verifyLiabilityProtectionVASCardIsIncluded() {
		Assert.assertTrue(elementExists(liabilityProtectionIncludedText, 40), "Liability Protection VAS card is not included from account profile");
	}
	
	protected void verifyLiabilityProtectionVASCardIsNotIncluded() {
		Assert.assertFalse(elementExists(liabilityProtectionIncludedText, 2), "Liability Protection VAS card is included from account profile though it is not expected");
	}
	
	protected void verifyLiabilityProtectionVASCardPriceIsDisplayed() {
		Assert.assertTrue(elementExists(liabilityProtectionPriceText, 40), "Liability Protection price details is not displayed");
	}
	
	protected void verifyLiabilityProtectionVASCardPriceIsNotDisplayed() {
		Assert.assertFalse(elementExists(liabilityProtectionPriceText, 2), "Liability Protection price is displayed even after it is added/included");
	}
	
	protected void verifyLiabilityProtectionVASAddButtonIsDisplayed() {
		Assert.assertTrue(elementExists(liabilityProtectionAddButton, 40), "Liability Protection Add button is not displayed");
	}
	
	protected void verifyLiabilityProtectionVASAddedButtonIsDisplayed() {
		Assert.assertTrue(elementExists(liabilityProtectionAddedButton, 40), "Liability Protection Add button is not displayed");
	}
	
	protected void verifyLiabilityProtectionVASAddButtonNotDisplayed() {
		Assert.assertFalse(elementExists(liabilityProtectionAddButton, 2), "Liability Protection Add button is displayed even after it is added/included");
	}
	
	protected void addLiabilityProtection() {
		clickElement(liabilityProtectionVASCardText);;
	}
	
	protected void verifyLiabilityProtectionSocialProofingIsDisplayed() {
		Assert.assertTrue(elementExists(liabilityProtectionSocialProofingText, 40), "Protect your car Add button is not displayed");
	}
	
	protected void clickLiabilityProtectionInfo() {
		clickElement(liabilityProtectionInfoLink);;
	}
	
	protected void verifyLiabilityProtectionInfoScreenIsDisplayed() {
		Assert.assertTrue(getElementCount(liabilityProtectionInfoScreenText)==2, "Liability Protection info screen is not displayed");
	}
	
	protected void clickLiabilityProtectionInfoClose() {
		clickElement(liabilityProtectionInfoCloseButton);;
	}
	
	
	protected void verifyPersonalProtectionPackageVASCardDisplayed() {
		Assert.assertTrue(elementExists(personalProtectionPackageVASCardText, 40), "Personal Protection Package VAS card is not correct/displayed");
	}
	
	protected void verifyPersonalProtectionPackageVASCardContentDisplayed() {
		Assert.assertTrue(elementExists(personalProtectionPackageVASContentText, 40), "Personal Protection Package VAS card content is not correct/Displayed");
	}
	
	protected void verifyPersonalProtectionPackageVASCardIsIncluded() {
		Assert.assertTrue(elementExists(personalProtectionPackageIncludedText, 40), "Personal Protection Package VAS card is not included from account profile");
	}
	
	protected void verifyPersonalProtectionPackageVASCardIsNotIncluded() {
		Assert.assertFalse(elementExists(personalProtectionPackageIncludedText, 2), "Personal Protection Package VAS card is included from account profile though it is not expected");
	}
	
	protected void verifyPersonalProtectionPackageVASCardPriceIsDisplayed() {
		Assert.assertTrue(elementExists(personalProtectionPackagePriceText, 40), "Personal Protection Package price details is not displayed");
	}
	
	protected void verifyPersonalProtectionPackageVASCardPriceIsNotDisplayed() {
		Assert.assertFalse(elementExists(personalProtectionPackagePriceText, 2), "Personal Protection Package price is displayed even after it is added/included");
	}
	
	protected void verifyPersonalProtectionPackageVASAddButtonIsDisplayed() {
		Assert.assertTrue(elementExists(personalProtectionPackageAddButton, 40), "Personal Protection Package Add button is not displayed");
	}
	
	protected void verifyPersonalProtectionPackageVASAddedButtonIsDisplayed() {
		Assert.assertTrue(elementExists(personalProtectionPackageAddedButton, 40), "Personal Protection Package Add button is not displayed");
	}
	
	protected void verifyPersonalProtectionPackageVASAddButtonNotDisplayed() {
		Assert.assertFalse(elementExists(personalProtectionPackageAddButton, 2), "Personal Protection Package Add button is displayed even after it is added/included");
	}
	
	protected void addPersonalProtectionPackage() {
		clickElement(personalProtectionPackageVASCardText);;
	}
	
	protected void verifyPersonalProtectionPackageSocialProofingIsDisplayed() {
		Assert.assertTrue(elementExists(personalProtectionPackageSocialProofingText, 40), "Protect your car Add button is not displayed");
	}
	
	protected void clickPersonalProtectionPackageInfo() {
		clickElement(personalProtectionPackageInfoLink);;
	}
	
	protected void verifyPersonalProtectionPackageInfoScreenIsDisplayed() {
		Assert.assertTrue(getElementCount(personalProtectionPackageInfoScreenText)==2, "Protect the car info screen is not displayed");
	}
	
	protected void clickPersonalProtectionPackageInfoClose() {
		clickElement(personalProtectionPackageInfoCloseButton);
	}
	
	
	protected void verifyDriveWithTotalPeaceOfMindVASCardDisplayed() {
		swipeScreen(Direction.UP);
		Assert.assertTrue(elementExists(driveWithTotalPeaceOfMindVASCardText, 40, "Drive with total peace of mind"), "Drive With Total Peace Of Mind VAS card is not correct/displayed");
	}
	
	protected void verifyDriveWithTotalPeaceOfMindVASCardContentDisplayed() {
		Assert.assertTrue(elementExists(driveWithTotalPeaceOfMindVASContentText, 40,"Reduce your"), "Drive With Total Peace Of Mind VAS card content is not correct/Displayed");
	}
	
	protected void verifyDriveWithTotalPeaceOfMindVASCardIsIncluded() {
		Assert.assertTrue(elementExists(driveWithTotalPeaceOfMindIncludedText, 40), "Drive With Total Peace Of Mind VAS card is not included from account profile");
	}
	
	protected void verifyDriveWithTotalPeaceOfMindVASCardIsNotIncluded() {
		Assert.assertFalse(elementExists(driveWithTotalPeaceOfMindIncludedText, 2), "Drive With Total Peace Of Mind VAS card is included from account profile though it is not expected");
	}
	
	protected void verifyDriveWithTotalPeaceOfMindVASCardPriceIsDisplayed() {
		Assert.assertTrue(elementExists(driveWithTotalPeaceOfMindPriceText, 40), "Drive With Total Peace Of Mind price details is not displayed");
	}
	
	protected void verifyDriveWithTotalPeaceOfMindVASCardPriceIsNotDisplayed() {
		Assert.assertFalse(elementExists(driveWithTotalPeaceOfMindPriceText, 2), "Drive With Total Peace Of Mind price is displayed even after it is added/included");
	}
	
	protected void verifyDriveWithTotalPeaceOfMindVASAddButtonIsDisplayed() {
		Assert.assertTrue(elementExists(driveWithTotalPeaceOfMindAddButton, 40), "Drive With Total Peace Of Mind Add button is not displayed");
	}
	
	protected void verifyDriveWithTotalPeaceOfMindVASAddedButtonIsDisplayed() {
		Assert.assertTrue(elementExists(driveWithTotalPeaceOfMindAddedButton, 40), "Drive With Total Peace Of Mind Add button is not displayed");
	}
	
	protected void verifyDriveWithTotalPeaceOfMindVASAddButtonNotDisplayed() {
		Assert.assertFalse(elementExists(driveWithTotalPeaceOfMindAddButton, 2), "Drive With Total Peace Of Mind Add button is displayed even after it is added/included");
	}
	
	protected void addDriveWithTotalPeaceOfMind() {
		clickElement(driveWithTotalPeaceOfMindVASContentText);;
	}
	
	protected void verifyDriveWithTotalPeaceOfMindSocialProofingIsNotDisplayed() {
		Assert.assertFalse(elementExists(driveWithTotalPeaceOfMindSocialProofingText, 3), "Protect your car Add button is not displayed");
	}
	
	protected void clickDriveWithTotalPeaceOfMindInfo() {
		clickElement(driveWithTotalPeaceOfMindInfoLink);;
	}
	
	protected void verifyDriveWithTotalPeaceOfMindInfoScreenIsDisplayed() {
		Assert.assertTrue(getElementCount(driveWithTotalPeaceOfMindInfoScreenText)==2, "Frive with total peace of mind info screen is not displayed");
	}
	
	protected void clickDriveWithTotalPeaceOfMindInfoClose() {
		clickElement(driveWithTotalPeaceOfMindInfoCloseButton);;
	}
	
	
	protected void verifyLossDamageWaiverVASCardDisplayed() {
		Assert.assertTrue(elementExists(lossDamageWaiverVASCardText, 40), "Loss Damage Waiver VAS card is not correct/displayed");
	}

	protected void verifyLossDamageWaiverVASCardContentDisplayed() {
		Assert.assertTrue(elementExists(lossDamageWaiverVASContentText, 40), "Loss Damage Waiver VAS card content is not correct/Displayed");
	}

	protected void verifyLossDamageWaiverVASCardIsIncluded() {
		Assert.assertTrue(elementExists(lossDamageWaiverIncludedText, 40), "Loss Damage Waiver VAS card is not included from account profile");
	}

	protected void verifyLossDamageWaiverVASCardIsNotIncluded() {
		Assert.assertFalse(elementExists(lossDamageWaiverIncludedText, 2), "Loss Damage Waiver VAS card is included from account profile though it is not expected");
	}

	protected void verifyLossDamageWaiverVASCardPriceIsDisplayed() {
		Assert.assertTrue(elementExists(lossDamageWaiverPriceText, 40), "Loss Damage Waiver price details is not displayed");
	}

	protected void verifyLossDamageWaiverVASCardPriceIsNotDisplayed() {
		Assert.assertFalse(elementExists(lossDamageWaiverPriceText, 2), "Loss Damage Waiver price is displayed even after it is added/included");
	}

	protected void verifyLossDamageWaiverVASAddButtonIsDisplayed() {
		Assert.assertTrue(elementExists(lossDamageWaiverAddButton, 40), "Loss Damage Waiver Add button is not displayed");
	}

	protected void verifyLossDamageWaiverVASAddedButtonIsDisplayed() {
		Assert.assertTrue(elementExists(lossDamageWaiverAddedButton, 40), "Loss Damage Waiver Add button is not displayed");
	}

	protected void verifyLossDamageWaiverVASAddButtonNotDisplayed() {
		Assert.assertFalse(elementExists(lossDamageWaiverAddButton, 2), "Loss Damage Waiver Add button is displayed even after it is added/included");
	}

	protected void addlossDamageWaiver() {
		clickElement(lossDamageWaiverVASCardText);;
	}

	protected void verifyLossDamageWaiverSocialProofingIsNotDisplayed() {
		Assert.assertFalse(elementExists(lossDamageWaiverSocialProofingText, 2), "Loss Damage Waiver social proofing is displayed");
	}

	protected void clickLossDamageWaiverInfo() {
		clickElement(lossDamageWaiverInfoLink);;
	}

	protected void verifyLossDamageWaiverInfoScreenIsDisplayed() {
		Assert.assertTrue(getElementCount(lossDamageWaiverInfoScreenText)==2, "Loss Damage waier info screen is not displayed");
	}

	protected void clickLossDamageWaiverInfoClose() {
		clickElement(lossDamageWaiverInfoCloseButton);;
	}
		
		
	protected void verifyContinueWithoutProtectionCardDisplayed() {
		Assert.assertTrue(elementExists(continueWithoutProtectionCardText, 40), "Continue without protection card is not correct/displayed");
	}

	protected void verifyContinueWithoutProtectionCardContentDisplayed() {
		Assert.assertTrue(elementExists(continueWithoutProtectionContentText, 40), "Loss Damage Waiver VAS card content is not correct/Displayed");
	}
	
	protected void clickContinueWithoutProtectionInfo() {
		clickElement(continueWithoutProtectionInfoLink);;
	}

	protected void verifyContinueWithoutProtectionInfoScreenIsDisplayed() {
		Assert.assertTrue(elementExists(continueWithoutProtectionInfoScreenText,2), "Protect the car info screen is not displayed");
	}

	protected void clickContinueWithoutProtectionInfoClose() {
		clickElement(continueWithoutProtectionInfoCloseButton);;
	}
		
	protected void clickContinueWithoutProtectionCheckBox() {
		clickElement(continueWithoutProtectionCheckbox);
	}
	
	
	protected void clickContinue() {
		clickElement(continueButton);
	}
	
	protected void verifyContinueButtonIsDisabled() {
		Assert.assertTrue(getAttributeValueOnElement(parentOfcontinueButton, "enabled").contentEquals("false"), "Continue button is enabled without any VAS item selected");
	}
	
	protected void verifyContinueButtonIsEnabled() {
		Assert.assertTrue(getAttributeValueOnElement(parentOfcontinueButton, "enabled").contentEquals("true"), "Continue button is disabled even after selecting VAS/Checkbox");
	}
	
	protected void verifyAddForButtonExists() {
		elementExists(addForButtonInfoScreenButton, 5);
	}

	protected void clickAddForButtonInfo() {
		clickElement(addForButtonInfoScreenButton);
	}
	
	protected void verifyAddedButtonExists() {
		elementExists(addedButtonInfoScreenButton, 5);
	}

	protected void clickAddedButtonInfo() {
		clickElement(addedButtonInfoScreenButton);
	}
}
