package com.pageobjects.HertzScreens;

import org.openqa.selenium.By;
import org.testng.Assert;

import com.framework.reusable.MobileResuableComponents;

public class ImproveYourTripScreen extends MobileResuableComponents {

	By improveYourTripScreenTitleText = By.xpath("//android.widget.TextView[@text='Improve Your Trip']");
	
	By FPOVASCardText = By.xpath("//android.widget.TextView[@text='Rental Extras']//following-sibling::android.view.View/android.widget.TextView[@text='Skip the Pump and Save Time']");
	By FPOVASContentText = By.xpath("//android.widget.TextView[@text='Rental Extras']//following-sibling::android.view.View/android.widget.TextView[@text='Skip the Pump and Save Time']/following-sibling::android.widget.TextView[contains(@text,'Pay for gas now')]");
	By FPOIncludedText = By.xpath("//android.widget.TextView[@text='Rental Extras']//following-sibling::android.view.View/android.widget.TextView[@text='Skip the Pump and Save Time']/following-sibling::android.widget.TextView[@text='Included']");
	By FPOPriceText = By.xpath("//android.widget.TextView[@text='Rental Extras']//following-sibling::android.view.View/android.widget.TextView[@text='Skip the Pump and Save Time']/following-sibling::android.widget.TextView[contains(@text,'/day')]");
	By FPOAddButton = By.xpath("//android.widget.TextView[@text='Rental Extras']//following-sibling::android.view.View/android.widget.TextView[@text='Skip the Pump and Save Time']/following-sibling::android.view.View/android.widget.TextView[@text='Add']/../android.widget.Button");
	By FPOAddedButton = By.xpath("//android.widget.TextView[@text='Rental Extras']//following-sibling::android.view.View/android.widget.TextView[@text='Skip the Pump and Save Time']/following-sibling::android.view.View/android.widget.TextView[@text='Added']/../android.widget.Button");
	By FPOSocialProofingText = By.xpath("//android.widget.TextView[@text='Rental Extras']//following-sibling::android.view.View/android.widget.TextView[@text='Skip the Pump and Save Time']/following-sibling::android.widget.TextView[contains(@text,'added last month')]");
	By FPOInfoLink = By.xpath("//android.widget.TextView[@text='Rental Extras']//following-sibling::android.view.View/android.widget.TextView[@text='Skip the Pump and Save Time']/../following-sibling::android.view.View[1]/android.widget.Button");
	By FPOInfoScreenText = By.xpath("//android.widget.TextView[@text='Skip the Pump and Save Time']");
	By FPOInfoCloseButton = By.xpath("//android.widget.TextView[@text='Skip the Pump and Save Time']/following-sibling::android.widget.Button");
	
	
	public ImproveYourTripScreen() {
		super();
	}

	protected void verifyImproveYourTripScreenDisplayed() {
		Assert.assertTrue(elementExists(improveYourTripScreenTitleText, 40), "Improve Your Trip screen is not displayed");
	}
	
	protected void verifyFPOVASCardDisplayed() {
		Assert.assertTrue(elementExists(FPOVASCardText, 40), "FPO VAS card is not correct/displayed");
	}
	
	protected void verifyFPOVASCardContentDisplayed() {
		Assert.assertTrue(elementExists(FPOVASContentText, 40), "FPO VAS card content is not correct/Displayed");
	}
	
	protected void verifyFPOVASCardIsIncluded() {
		Assert.assertTrue(elementExists(FPOIncludedText, 40), "FPO VAS card is not included from account profile");
	}
	
	protected void verifyFPOVASCardIsNotIncluded() {
		Assert.assertFalse(elementExists(FPOIncludedText, 2), "FPO VAS card is included from account profile though it is not expected");
	}
	
	protected void verifyFPOVASCardPriceIsDisplayed() {
		Assert.assertTrue(elementExists(FPOPriceText, 40), "FPO price details is not displayed");
	}
	
	protected void verifyFPOVASCardPriceIsNotDisplayed() {
		Assert.assertFalse(elementExists(FPOPriceText, 2), "FPO price is displayed even after it is added/included");
	}
	
	protected void verifyFPOVASAddButtonIsDisplayed() {
		Assert.assertTrue(elementExists(FPOAddButton, 40), "FPO Add button is not displayed");
	}
	
	protected void verifyFPOVASAddedButtonIsDisplayed() {
		Assert.assertTrue(elementExists(FPOAddedButton, 40), "FPO Add button is not displayed");
	}
	
	protected void verifyFPOVASAddButtonNotDisplayed() {
		Assert.assertFalse(elementExists(FPOAddButton, 2), "FPO Add button is displayed even after it is added/included");
	}
	
	protected void addFPO() {
		clickElement(FPOVASCardText);;
	}
	
	protected void verifyFPOSocialProofingIsDisplayed() {
		Assert.assertTrue(elementExists(FPOSocialProofingText, 40), "FPO Add button is not displayed");
	}
	
	protected void clickFPOInfo() {
		clickElement(FPOInfoLink);;
	}
	
	protected void verifyFPOInfoScreenIsDisplayed() {
		Assert.assertTrue(getElementCount(FPOInfoScreenText)==2, "FPO info screen is not displayed");
	}
	
	protected void clickFPOInfoClose() {
		clickElement(FPOInfoCloseButton);;
	}
	
	
	By SiriusXMVASCardText = By.xpath("//android.widget.TextView[@text='Rental Extras']//following-sibling::android.view.View//android.widget.TextView[contains(@text,'SiriusXM')]");
	By SiriusXMVASContentText = By.xpath("//android.widget.TextView[@text='Rental Extras']//following-sibling::android.view.View//android.widget.TextView[contains(@text,'SiriusXM')]/following-sibling::android.widget.TextView[contains(@text,'satellite radio')]");
	By SiriusXMIncludedText = By.xpath("//android.widget.TextView[@text='Rental Extras']//following-sibling::android.view.View//android.widget.TextView[contains(@text,'SiriusXM')']/following-sibling::android.widget.TextView[@text='Included']");
	By SiriusXMPriceText = By.xpath("//android.widget.TextView[@text='Rental Extras']//following-sibling::android.view.View//android.widget.TextView[contains(@text,'SiriusXM')]/following-sibling::android.widget.TextView[contains(@text,'/day')]");
	By SiriusXMAddButton = By.xpath("//android.widget.TextView[@text='Rental Extras']//following-sibling::android.view.View//android.widget.TextView[contains(@text,'SiriusXM')]/following-sibling::android.view.View/android.widget.TextView[@text='Add']/../android.widget.Button");
	By SiriusXMAddedButton = By.xpath("//android.widget.TextView[@text='Rental Extras']//following-sibling::android.view.View//android.widget.TextView[contains(@text,'SiriusXM')]/following-sibling::android.view.View/android.widget.TextView[@text='Added']/../android.widget.Button");
	By SiriusXMSocialProofingText = By.xpath("//android.widget.TextView[@text='Rental Extras']//following-sibling::android.view.View//android.widget.TextView[contains(@text,'SiriusXM')]/following-sibling::android.widget.TextView[contains(@text,'added last month')]");
	By SiriusXMInfoLink = By.xpath("//android.widget.TextView[@text='Rental Extras']//following-sibling::android.view.View//android.widget.TextView[contains(@text,'SiriusXM')]/../following-sibling::android.view.View[1]/android.widget.Button");
	By SiriusXMInfoScreenText = By.xpath("//android.widget.TextView[@text='SiriusXM®']");
	By SiriusXMInfoCloseButton = By.xpath("//android.widget.TextView[@text='SiriusXM®']/following-sibling::android.widget.Button");
	
	protected void verifySiriusXMVASCardDisplayed() {
		Assert.assertTrue(elementExists(SiriusXMVASCardText, 40), "SiriusXM VAS card is not correct/displayed");
	}
	
	protected void verifySiriusXMVASCardContentDisplayed() {
		Assert.assertTrue(elementExists(SiriusXMVASContentText, 40), "SiriusXM VAS card content is not correct/Displayed");
	}
	
	protected void verifySiriusXMVASCardIsIncluded() {
		Assert.assertTrue(elementExists(SiriusXMIncludedText, 40), "SiriusXM VAS card is not included from account profile");
	}
	
	protected void verifySiriusXMVASCardIsNotIncluded() {
		Assert.assertFalse(elementExists(SiriusXMIncludedText, 2), "SiriusXM VAS card is included from account profile though it is not expected");
	}
	
	protected void verifySiriusXMVASCardPriceIsDisplayed() {
		Assert.assertTrue(elementExists(SiriusXMPriceText, 40), "SiriusXM price details is not displayed");
	}
	
	protected void verifySiriusXMVASCardPriceIsNotDisplayed() {
		Assert.assertFalse(elementExists(SiriusXMPriceText, 2), "SiriusXM price is displayed even after it is added/included");
	}
	
	protected void verifySiriusXMVASAddButtonIsDisplayed() {
		Assert.assertTrue(elementExists(SiriusXMAddButton, 40), "SiriusXM Add button is not displayed");
	}
	
	protected void verifySiriusXMVASAddedButtonIsDisplayed() {
		Assert.assertTrue(elementExists(SiriusXMAddedButton, 40), "SiriusXM Add button is not displayed");
	}
	
	protected void verifySiriusXMVASAddButtonNotDisplayed() {
		Assert.assertFalse(elementExists(SiriusXMAddButton, 2), "SiriusXM Add button is displayed even after it is added/included");
	}
	
	protected void addSiriusXM() {
		clickElement(SiriusXMVASCardText);;
	}
	
	protected void verifySiriusXMSocialProofingIsNotDisplayed() {
		Assert.assertFalse(elementExists(SiriusXMSocialProofingText, 2), "SiriusXM social proofing is displayed");
	}
	
	protected void clickSiriusXMInfo() {
		clickElement(SiriusXMInfoLink);;
	}
	
	protected void verifySiriusXMInfoScreenIsDisplayed() {
		Assert.assertTrue(getElementCount(SiriusXMInfoScreenText)==2, "SiriusXM info screen is not displayed");
	}
	
	protected void clickSiriusXMInfoClose() {
		clickElement(SiriusXMInfoCloseButton);;
	}
	
	By UnlimitedWiFiVASCardText = By.xpath("//android.widget.TextView[@text='Rental Extras']//following-sibling::android.view.View//android.widget.TextView[@text='Unlimited Wi-Fi — Stay Connected']");
	By UnlimitedWiFiVASContentText = By.xpath("//android.widget.TextView[@text='Rental Extras']//following-sibling::android.view.View//android.widget.TextView[@text='Unlimited Wi-Fi — Stay Connected']/following-sibling::android.widget.TextView[contains(@text,'GPS device')]");
	By UnlimitedWiFiIncludedText = By.xpath("//android.widget.TextView[@text='Rental Extras']//following-sibling::android.view.View//android.widget.TextView[@text='Unlimited Wi-Fi — Stay Connected']/following-sibling::android.widget.TextView[@text='Included']");
	By UnlimitedWiFiPriceText = By.xpath("//android.widget.TextView[@text='Rental Extras']//following-sibling::android.view.View//android.widget.TextView[@text='Unlimited Wi-Fi — Stay Connected']/following-sibling::android.widget.TextView[contains(@text,'/day')]");
	By UnlimitedWiFiAddButton = By.xpath("//android.widget.TextView[@text='Rental Extras']//following-sibling::android.view.View//android.widget.TextView[@text='Unlimited Wi-Fi — Stay Connected']/following-sibling::android.view.View/android.widget.TextView[@text='Add']/../android.widget.Button");
	By UnlimitedWiFiAddedButton = By.xpath("//android.widget.TextView[@text='Rental Extras']//following-sibling::android.view.View//android.widget.TextView[@text='Unlimited Wi-Fi — Stay Connected']/following-sibling::android.view.View/android.widget.TextView[@text='Added']/../android.widget.Button");
	By UnlimitedWiFiSocialProofingText = By.xpath("//android.widget.TextView[@text='Rental Extras']//following-sibling::android.view.View//android.widget.TextView[@text='Unlimited Wi-Fi — Stay Connected']/following-sibling::android.widget.TextView[contains(@text,'added last month')]");
	By UnlimitedWiFiInfoLink = By.xpath("//android.widget.TextView[@text='Rental Extras']//following-sibling::android.view.View//android.widget.TextView[@text='Unlimited Wi-Fi — Stay Connected']/../following-sibling::android.view.View[1]/android.widget.Button");
	By UnlimitedWiFiInfoScreenText = By.xpath("//android.widget.TextView[@text='Unlimited Wi-Fi — Stay Connected']");
	By UnlimitedWiFiInfoCloseButton = By.xpath("//android.widget.TextView[@text='Unlimited Wi-Fi — Stay Connected']/following-sibling::android.widget.Button");
	
	protected void verifyUnlimitedWiFiVASCardDisplayed() {
		Assert.assertTrue(elementExists(UnlimitedWiFiVASCardText, 40), "UnlimitedWiFi VAS card is not correct/displayed");
	}
	
	protected void verifyUnlimitedWiFiVASCardContentDisplayed() {
		Assert.assertTrue(elementExists(UnlimitedWiFiVASContentText, 40), "UnlimitedWiFi VAS card content is not correct/Displayed");
	}
	
	protected void verifyUnlimitedWiFiVASCardIsIncluded() {
		Assert.assertTrue(elementExists(UnlimitedWiFiIncludedText, 40), "UnlimitedWiFi VAS card is not included from account profile");
	}
	
	protected void verifyUnlimitedWiFiVASCardIsNotIncluded() {
		Assert.assertFalse(elementExists(UnlimitedWiFiIncludedText, 2), "UnlimitedWiFi VAS card is included from account profile though it is not expected");
	}
	
	protected void verifyUnlimitedWiFiVASCardPriceIsDisplayed() {
		Assert.assertTrue(elementExists(UnlimitedWiFiPriceText, 40), "UnlimitedWiFi price details is not displayed");
	}
	
	protected void verifyUnlimitedWiFiVASCardPriceIsNotDisplayed() {
		Assert.assertFalse(elementExists(UnlimitedWiFiPriceText, 2), "UnlimitedWiFi price is displayed even after it is added/included");
	}
	
	protected void verifyUnlimitedWiFiVASAddButtonIsDisplayed() {
		Assert.assertTrue(elementExists(UnlimitedWiFiAddButton, 40), "UnlimitedWiFi Add button is not displayed");
	}
	
	protected void verifyUnlimitedWiFiVASAddedButtonIsDisplayed() {
		Assert.assertTrue(elementExists(UnlimitedWiFiAddedButton, 40), "UnlimitedWiFi Add button is not displayed");
	}
	
	protected void verifyUnlimitedWiFiVASAddButtonNotDisplayed() {
		Assert.assertFalse(elementExists(UnlimitedWiFiAddButton, 2), "UnlimitedWiFi Add button is displayed even after it is added/included");
	}
	
	protected void addUnlimitedWiFi() {
		clickElement(UnlimitedWiFiVASCardText);;
	}
	
	protected void verifyUnlimitedWiFiSocialProofingIsNotDisplayed() {
		Assert.assertFalse(elementExists(UnlimitedWiFiSocialProofingText, 2), "UnlimitedWiFi Social proofing is displayed");
	}
	
	protected void clickUnlimitedWiFiInfo() {
		clickElement(UnlimitedWiFiInfoLink);;
	}
	
	protected void verifyUnlimitedWiFiInfoScreenIsDisplayed() {
		Assert.assertTrue(getElementCount(UnlimitedWiFiInfoScreenText)==2, "UnlimitedWiFi info screen is not displayed");
	}
	
	protected void clickUnlimitedWiFiInfoClose() {
		clickElement(UnlimitedWiFiInfoCloseButton);;
	}
	
	By BoosterSeatVASCardText = By.xpath("//android.widget.TextView[@text='Child Seats']//following-sibling::android.view.View//android.widget.TextView[@text='Booster Seat']");
	By BoosterSeatVASContentText = By.xpath("//android.widget.TextView[@text='Child Seats']//following-sibling::android.view.View//android.widget.TextView[@text='Booster Seat']/following-sibling::android.widget.TextView[contains(@text,'40 to 80')]");
	By BoosterSeatIncludedText = By.xpath("//android.widget.TextView[@text='Child Seats']//following-sibling::android.view.View//android.widget.TextView[@text='Booster Seat']/following-sibling::android.widget.TextView[@text='Included']");
	By BoosterSeatPriceText = By.xpath("//android.widget.TextView[@text='Child Seats']//following-sibling::android.view.View//android.widget.TextView[@text='Booster Seat']/following-sibling::android.widget.TextView[contains(@text,'/day')]");
	By BoosterSeatAddButton = By.xpath("//android.widget.TextView[@text='Child Seats']//following-sibling::android.view.View//android.widget.TextView[@text='Booster Seat']/following-sibling::android.view.View/android.widget.TextView[@text='Add']/../android.widget.Button");
	By BoosterSeatCounterButton = By.xpath("//android.widget.TextView[@text='Child Seats']//following-sibling::android.view.View//android.widget.TextView[@text='Booster Seat']//following-sibling::android.widget.Button");
	By BoosterSeatSocialProofingText = By.xpath("//android.widget.TextView[@text='Child Seats']//following-sibling::android.view.View//android.widget.TextView[@text='Booster Seat']/following-sibling::android.widget.TextView[contains(@text,'added last month')]");
	By BoosterSeatInfoLink = By.xpath("//android.widget.TextView[@text='Child Seats']//following-sibling::android.view.View//android.widget.TextView[@text='Booster Seat']/../following-sibling::android.view.View[1]/android.widget.Button");
	By BoosterSeatInfoScreenText = By.xpath("//android.widget.TextView[@text='Booster Seat']");
	By BoosterSeatInfoCloseButton = By.xpath("//android.widget.TextView[@text='Booster Seat']/following-sibling::android.widget.Button");
	
	protected void verifyBoosterSeatVASCardDisplayed() {
		swipeUntilElementExists(BoosterSeatAddButton);
		Assert.assertTrue(elementExists(BoosterSeatVASCardText, 40,"Booster Seat"), "BoosterSeat VAS card is not correct/displayed");
	}
	
	protected void verifyBoosterSeatVASCardContentDisplayed() {
		Assert.assertTrue(elementExists(BoosterSeatVASContentText, 40,"Booster Seat"), "BoosterSeat VAS card content is not correct/Displayed");
	}
	
	protected void verifyBoosterSeatVASCardIsIncluded() {
		Assert.assertTrue(elementExists(BoosterSeatIncludedText, 40,"Booster Seat"), "BoosterSeat VAS card is not included from account profile");
	}
	
	protected void verifyBoosterSeatVASCardIsNotIncluded() {
		Assert.assertFalse(elementExists(BoosterSeatIncludedText, 2,"Booster Seat"), "BoosterSeat VAS card is included from account profile though it is not expected");
	}
	
	protected void verifyBoosterSeatVASCardPriceIsDisplayed() {
		Assert.assertTrue(elementExists(BoosterSeatPriceText, 40,"Booster Seat"), "BoosterSeat price details is not displayed");
	}
	
	protected void verifyBoosterSeatVASCardPriceIsNotDisplayed() {
		Assert.assertFalse(elementExists(BoosterSeatPriceText, 2,"Booster Seat"), "BoosterSeat price is displayed even after it is added/included");
	}
	
	protected void verifyBoosterSeatVASAddButtonIsDisplayed() {
		Assert.assertTrue(elementExists(BoosterSeatAddButton, 40,"Booster Seat"), "BoosterSeat Add button is not displayed");
	}
	
	protected void verifyBoosterSeatVASCounterButtonIsDisplayed() {
		Assert.assertTrue(getElementCount(BoosterSeatCounterButton)==2, "BoosterSeat Add button is not displayed");
	}
	
	protected void verifyBoosterSeatVASAddButtonNotDisplayed() {
		Assert.assertFalse(elementExists(BoosterSeatAddButton, 2,"Booster Seat"), "BoosterSeat Add button is displayed even after it is added/included");
	}
	
	protected void addBoosterSeat() {
		scrollToElementText("Booster Seat");
		clickElement(BoosterSeatVASCardText);;
	}
	
	protected void verifyBoosterSeatSocialProofingIsNotDisplayed() {
		Assert.assertFalse(elementExists(BoosterSeatSocialProofingText, 2), "Booster Seat social proofing is displayed");
	}
	
	protected void clickBoosterSeatInfo() {
		scrollToElementText("Booster Seat");
		clickElement(BoosterSeatInfoLink);;
	}
	
	protected void verifyBoosterSeatInfoScreenIsDisplayed() {
		Assert.assertTrue(getElementCount(BoosterSeatInfoScreenText)==2, "Booster Seat info screen is not displayed");
	}
	
	protected void clickBoosterSeatInfoClose() {
		clickElement(BoosterSeatInfoCloseButton);;
	}
	
	By ChildSeatVASCardText = By.xpath("//android.widget.TextView[@text='Child Seats']//following-sibling::android.view.View//android.widget.TextView[@text='Child Seat']");
	By ChildSeatVASContentText = By.xpath("//android.widget.TextView[@text='Child Seats']//following-sibling::android.view.View//android.widget.TextView[@text='Child Seat']/following-sibling::android.widget.TextView[contains(@text,'20-40')]");
	By ChildSeatIncludedText = By.xpath("//android.widget.TextView[@text='Child Seats']//following-sibling::android.view.View//android.widget.TextView[@text='Child Seat']/following-sibling::android.widget.TextView[@text='Included']");
	By ChildSeatPriceText = By.xpath("//android.widget.TextView[@text='Child Seats']//following-sibling::android.view.View//android.widget.TextView[@text='Child Seat']/following-sibling::android.widget.TextView[contains(@text,'/day')]");
	By ChildSeatAddButton = By.xpath("//android.widget.TextView[@text='Child Seats']//following-sibling::android.view.View//android.widget.TextView[@text='Child Seat']/following-sibling::android.view.View/android.widget.TextView[@text='Add']/../android.widget.Button");
	By ChildSeatCounterButton = By.xpath("//android.widget.TextView[@text='Child Seats']//following-sibling::android.view.View//android.widget.TextView[@text='Child Seat']/following-sibling::android.widget.Button");
	By ChildSeatSocialProofingText = By.xpath("//android.widget.TextView[@text='Child Seats']//following-sibling::android.view.View//android.widget.TextView[@text='Child Seat']/following-sibling::android.widget.TextView[contains(@text,'added last month')]");
	By ChildSeatInfoLink = By.xpath("//android.widget.TextView[@text='Child Seats']//following-sibling::android.view.View//android.widget.TextView[@text='Child Seat']/../following-sibling::android.view.View[1]/android.widget.Button");
	By ChildSeatInfoScreenText = By.xpath("//android.widget.TextView[@text='Child Seat']");
	By ChildSeatInfoCloseButton = By.xpath("//android.widget.TextView[@text='Child Seat']/following-sibling::android.widget.Button");
	
	protected void verifyChildSeatVASCardDisplayed() {
		swipeUntilElementExists(ChildSeatAddButton);
		Assert.assertTrue(elementExists(ChildSeatVASCardText, 40,"Child Seat"), "Child Seat VAS card is not correct/displayed");
	}
	
	protected void verifyChildSeatVASCardContentDisplayed() {
		Assert.assertTrue(elementExists(ChildSeatVASContentText, 40,"Child Seat"), "Child Seat VAS card content is not correct/Displayed");
	}
	
	protected void verifyChildSeatVASCardIsIncluded() {
		Assert.assertTrue(elementExists(ChildSeatIncludedText, 40,"Child Seat"), "Child Seat VAS card is not included from account profile");
	}
	
	protected void verifyChildSeatVASCardIsNotIncluded() {
		Assert.assertFalse(elementExists(ChildSeatIncludedText, 2,"Child Seat"), "Child Seat VAS card is included from account profile though it is not expected");
	}
	
	protected void verifyChildSeatVASCardPriceIsDisplayed() {
		Assert.assertTrue(elementExists(ChildSeatPriceText, 40,"Child Seat"), "Child Seat price details is not displayed");
	}
	
	protected void verifyChildSeatVASCardPriceIsNotDisplayed() {
		Assert.assertFalse(elementExists(ChildSeatPriceText, 2,"Child Seat"), "Child Seat price is displayed even after it is added/included");
	}
	
	protected void verifyChildSeatVASAddButtonIsDisplayed() {
		Assert.assertTrue(elementExists(ChildSeatAddButton, 40,"Child Seat"), "ChildSeat Add button is not displayed");
	}
	
	protected void verifyChildSeatVASCounterButtonIsDisplayed() {
		Assert.assertTrue(getElementCount(ChildSeatCounterButton)==2, "Child Seat Add button is not displayed");
	}
	
	protected void verifyChildSeatVASAddButtonNotDisplayed() {
		Assert.assertFalse(elementExists(ChildSeatAddButton, 2,"Child Seat"), "Child Seat Add button is displayed even after it is added/included");
	}
	
	protected void addChildSeat() {
		scrollToElementText("Child Seat");
		clickElement(ChildSeatVASCardText);;
	}
	
	protected void verifyChildSeatSocialProofingIsNotDisplayed() {
		Assert.assertFalse(elementExists(ChildSeatSocialProofingText, 2), "Child Seat social proofing is displayed");
	}
	
	protected void clickChildSeatInfo() {
		scrollToElementText("Child Seat");
		clickElement(ChildSeatInfoLink);;
	}
	
	protected void verifyChildSeatInfoScreenIsDisplayed() {
		Assert.assertTrue(getElementCount(ChildSeatInfoScreenText)==2, "ChildSeat info screen is not displayed");
	}
	
	protected void clickChildSeatInfoClose() {
		clickElement(ChildSeatInfoCloseButton);;
	}
	
	By InfantChildSeatVASCardText = By.xpath("//android.widget.TextView[@text='Child Seats']//following-sibling::android.view.View//android.widget.TextView[@text='Infant Child Seat']");
	By InfantChildSeatVASContentText = By.xpath("//android.widget.TextView[@text='Child Seats']//following-sibling::android.view.View//android.widget.TextView[@text='Infant Child Seat']/following-sibling::android.widget.TextView[contains(@text,'20 pounds')]");
	By InfantChildSeatIncludedText = By.xpath("//android.widget.TextView[@text='Child Seats']//following-sibling::android.view.View//android.widget.TextView[@text='Infant Child Seat']/following-sibling::android.widget.TextView[@text='Included']");
	By InfantChildSeatPriceText = By.xpath("//android.widget.TextView[@text='Child Seats']//following-sibling::android.view.View//android.widget.TextView[@text='Infant Child Seat']/following-sibling::android.widget.TextView[contains(@text,'/day')]");
	By InfantChildSeatAddButton = By.xpath("//android.widget.TextView[@text='Child Seats']//following-sibling::android.view.View//android.widget.TextView[@text='Infant Child Seat']/following-sibling::android.view.View/android.widget.TextView[@text='Add']/..");
	By InfantChildSeatCounterButton = By.xpath("//android.widget.TextView[@text='Child Seats']//following-sibling::android.view.View//android.widget.TextView[@text='Infant Child Seat']//following-sibling::android.widget.Button");
	By InfantChildSeatSocialProofingText = By.xpath("//android.widget.TextView[@text='Child Seats']//following-sibling::android.view.View//android.widget.TextView[@text='Infant Child Seat']/following-sibling::android.widget.TextView[contains(@text,'added last month')]");
	By InfantChildSeatInfoLink = By.xpath("//android.widget.TextView[@text='Child Seats']//following-sibling::android.view.View//android.widget.TextView[@text='Infant Child Seat']/../following-sibling::android.view.View[1]/android.widget.Button");
	By InfantChildSeatInfoScreenText = By.xpath("//android.widget.TextView[@text='Infant Child Seat']");
	By InfantChildSeatInfoCloseButton = By.xpath("//android.widget.TextView[@text='Infant Child Seat']/following-sibling::android.widget.Button");
	
	protected void verifyInfantChildSeatVASCardDisplayed() {
		swipeUntilElementExists(InfantChildSeatAddButton);
		Assert.assertTrue(elementExists(InfantChildSeatVASCardText, 40,"Infant Child Seat"), "Infant Child Seat VAS card is not correct/displayed");
	}
	
	protected void verifyInfantChildSeatVASCardContentDisplayed() {
		Assert.assertTrue(elementExists(InfantChildSeatVASContentText, 40,"Infant Child Seat"), "Infant Child Seat VAS card content is not correct/Displayed");
	}
	
	protected void verifyInfantChildSeatVASCardIsIncluded() {
		Assert.assertTrue(elementExists(InfantChildSeatIncludedText, 40,"Infant Child Seat"), "Infant Child Seat VAS card is not included from account profile");
	}
	
	protected void verifyInfantChildSeatVASCardIsNotIncluded() {
		Assert.assertFalse(elementExists(InfantChildSeatIncludedText, 2,"Infant Child Seat"), "Infant Child Seat VAS card is included from account profile though it is not expected");
	}
	
	protected void verifyInfantChildSeatVASCardPriceIsDisplayed() {
		Assert.assertTrue(elementExists(InfantChildSeatPriceText, 40,"Infant Child Seat"), "Infant Child Seat price details is not displayed");
	}
	
	protected void verifyInfantChildSeatVASCardPriceIsNotDisplayed() {
		Assert.assertFalse(elementExists(InfantChildSeatPriceText, 2,"Infant Child Seat"), "Infant Child Seat price is displayed even after it is added/included");
	}
	
	protected void verifyInfantChildSeatVASAddButtonIsDisplayed() {
		Assert.assertTrue(elementExists(InfantChildSeatAddButton, 40,"Infant Child Seat"), "Infant Child Seat Add button is not displayed");
	}
	
	protected void verifyInfantChildSeatVASCounterButtonIsDisplayed() {
		Assert.assertTrue(getElementCount(InfantChildSeatCounterButton)==2, "Infant Child Seat Add button is not displayed");
	}
	
	protected void verifyInfantChildSeatVASAddButtonNotDisplayed() {
		Assert.assertFalse(elementExists(InfantChildSeatAddButton, 2,"Infant Child Seat"), "Infant Child Seat Add button is displayed even after it is added/included");
	}
	
	protected void verifyInfantChildSeatVASAddButtonIsDisabled() {
		Assert.assertTrue(getAttributeValueOnElement(InfantChildSeatAddButton,"enabled").contentEquals("false"), "Infant Child Seat Add button is not disabled even after adding max number of VAS");
	}
	
	protected void addInfantChildSeat() {
		scrollToElementText("Infant Child Seat");
		clickElement(InfantChildSeatVASCardText);;
	}
	
	protected void verifyInfantChildSeatSocialProofingIsNotDisplayed() {
		Assert.assertFalse(elementExists(InfantChildSeatSocialProofingText, 2), "Infant Child Seat Social proofing is displayed");
	}
	
	protected void clickInfantChildSeatInfo() {
		scrollToElementText("Infant Child Seat");
		clickElement(InfantChildSeatInfoLink);;
	}
	
	protected void verifyInfantChildSeatInfoScreenIsDisplayed() {
		Assert.assertTrue(getElementCount(InfantChildSeatInfoScreenText)==2, "Infant Child Seat info screen is not displayed");
	}
	
	protected void clickInfantChildSeatInfoClose() {
		clickElement(InfantChildSeatInfoCloseButton);;
	}
	
	
	By WheelChairVASCardText = By.xpath("//android.widget.TextView[@text='Accessibility items']//following-sibling::android.view.View//android.widget.TextView[@text='Wheel chair']");
	By WheelChairVASContentText = By.xpath("//android.widget.TextView[@text='Accessibility items']//following-sibling::android.view.View//android.widget.TextView[@text='Wheel chair']/following-sibling::android.widget.TextView[contains(@text,'wheelchair')]");
	By WheelChairIncludedText = By.xpath("//android.widget.TextView[@text='Accessibility items']//following-sibling::android.view.View//android.widget.TextView[@text='Wheel chair']/following-sibling::android.widget.TextView[@text='Included']");
	By WheelChairPriceText = By.xpath("//android.widget.TextView[@text='Accessibility items']//following-sibling::android.view.View//android.widget.TextView[@text='Wheel chair']/following-sibling::android.widget.TextView[contains(@text,'/day')]");
	By WheelChairAddButton = By.xpath("//android.widget.TextView[@text='Accessibility items']//following-sibling::android.view.View//android.widget.TextView[@text='Wheel chair']/following-sibling::android.view.View/android.widget.TextView[@text='Add']/..");
	By WheelChairAddedButton = By.xpath("//android.widget.TextView[@text='Accessibility items']//following-sibling::android.view.View//android.widget.TextView[@text='Wheel chair']/following-sibling::android.view.View/android.widget.TextView[@text='Added']/../android.widget.Button");
	By WheelChairSocialProofingText = By.xpath("//android.widget.TextView[@text='Accessibility items']//following-sibling::android.view.View//android.widget.TextView[@text='Wheel chair']/following-sibling::android.widget.TextView[contains(@text,'added last month')]");
	By WheelChairInfoLink = By.xpath("//android.widget.TextView[@text='Accessibility items']//following-sibling::android.view.View//android.widget.TextView[@text='Wheel chair']/../following-sibling::android.view.View[1]/android.widget.Button");
	By WheelChairInfoScreenText = By.xpath("//android.widget.TextView[@text='Wheel chair']");
	By WheelChairInfoCloseButton = By.xpath("//android.widget.TextView[@text='Wheel chair']/following-sibling::android.widget.Button");
	
	protected void verifyWheelChairVASCardDisplayed() {
		swipeUntilElementExists(WheelChairAddButton);
		Assert.assertTrue(elementExists(WheelChairVASCardText, 40,"Wheel chair"), "Wheel chair VAS card is not correct/displayed");
	}
	
	protected void verifyWheelChairVASCardContentDisplayed() {
		Assert.assertTrue(elementExists(WheelChairVASContentText, 40,"Wheel chair"), "Wheel chair VAS card content is not correct/Displayed");
	}
	
	protected void verifyWheelChairVASCardIsIncluded() {
		Assert.assertTrue(elementExists(WheelChairIncludedText, 40,"Wheel chair"), "Wheel chair VAS card is not included from account profile");
	}
	
	protected void verifyWheelChairVASCardIsNotIncluded() {
		Assert.assertFalse(elementExists(WheelChairIncludedText, 2,"Wheel chair"), "Wheel chair VAS card is included from account profile though it is not expected");
	}
	
	protected void verifyWheelChairVASCardPriceIsDisplayed() {
		Assert.assertTrue(elementExists(WheelChairPriceText, 40,"Wheel chair"), "Wheel chair price details is not displayed");
	}
	
	protected void verifyWheelChairVASCardPriceIsNotDisplayed() {
		Assert.assertFalse(elementExists(WheelChairPriceText, 2,"Wheel chair"), "Wheel chair price is displayed even after it is added/included");
	}
	
	protected void verifyWheelChairVASAddButtonIsDisplayed() {
		Assert.assertTrue(elementExists(WheelChairAddButton, 40,"Wheel chair"), "Wheel chair Add button is not displayed");
	}
	
	protected void verifyWheelChairVASAddButtonIsDisabled() {
		Assert.assertTrue(getAttributeValueOnElement(WheelChairAddButton,"enabled").contentEquals("false"), "Wheel chair Add button is not disabled even after adding max number of VAS");
	}
	
	protected void verifyWheelChairVASAddedButtonIsDisplayed() {
		Assert.assertTrue(elementExists(WheelChairAddedButton, 40,"Wheel chair"), "Wheel chair Add button is not displayed");
	}
	
	protected void verifyWheelChairVASAddButtonNotDisplayed() {
		Assert.assertFalse(elementExists(WheelChairAddButton, 2,"Wheel chair"), "Wheel chair Add button is displayed even after it is added/included");
	}
	
	protected void addWheelChair() {
		scrollToElementText("Wheel chair");
		clickElement(WheelChairVASCardText);;
	}
	
	protected void verifyWheelChairSocialProofingIsNotDisplayed() {
		Assert.assertTrue(elementExists(WheelChairSocialProofingText, 2), "Wheel chair social proofing is displayed");
	}
	
	protected void clickWheelChairInfo() {
		scrollToElementText("Wheel chair");
		clickElement(WheelChairInfoLink);;
	}
	
	protected void verifyWheelChairInfoScreenIsDisplayed() {
		Assert.assertTrue(getElementCount(WheelChairInfoScreenText)==2, "Wheel chair info screen is not displayed");
	}
	
	protected void clickWheelChairInfoClose() {
		clickElement(WheelChairInfoCloseButton);;
	}
	
	By CPOVASCardText = By.xpath("//android.widget.TextView[@text='Rental Extras']/..//following-sibling::android.view.View/android.widget.TextView[@text=\"We’ll recharge if you don’t want to\"]");
	By CPOVASCardContentMemberText = By.xpath("//android.widget.TextView[@text='Rental Extras']/..//following-sibling::android.view.View/android.widget.TextView[contains(@text,'$25')]");
	By CPOVASCardContentNonMemberText = By.xpath("//android.widget.TextView[@text='Rental Extras']/..//following-sibling::android.view.View/android.widget.TextView[contains(@text,'$35')]");
	
	protected void verifyCPOVASCardIsDisplayed() {
		Assert.assertTrue(elementExists(CPOVASCardText, 40), "CPO VAS Card is not displayed");
	}
	
	protected void verifyCPOVASCardContentforMember() {
		Assert.assertTrue(elementExists(CPOVASCardContentMemberText, 40), "CPO VAS Card Content for Member is wrong");
	}
	
	protected void verifyCPOVASCardContentforNonMember() {
		Assert.assertTrue(elementExists(CPOVASCardContentNonMemberText, 40), "CPO VAS Card Content for Non Member is wrong");
	}
	
	
	By addForInfoScreenButton = By.xpath("//android.widget.TextView[contains(@text,'Add for')]/following-sibling::android.widget.Button/..");
	By addedInfoScreenButton = By.xpath("//android.widget.TextView[contains(@text,'Added')]/following-sibling::android.widget.Button");
	By CountersInfoScreenButton = By.xpath("//android.widget.TextView[contains(@text,'Seat')]/../..//following-sibling::android.widget.Button");
	By continueButton = By.xpath("//android.widget.TextView[@text='Continue']/following-sibling::android.widget.Button");
	By noThankYouButton = By.xpath("//android.widget.TextView[contains(@text,'No. Thank You')]/following-sibling::android.widget.Button");
	
	protected void clickAddButtonInforScreen() {
		clickElement(addForInfoScreenButton);;
	}
	
	protected void verifyAddButtonInforScreen() {
		Assert.assertTrue(elementExists(addForInfoScreenButton, 40), "Add button in VAS info screen is not displayed");
	}
	
	protected void verifyAddButtonInforIsDisabled() {
		Assert.assertTrue(getAttributeValueOnElement(addForInfoScreenButton,"enabled").contentEquals("false"), "Add button is not disabled even after adding max number of VAS in Info screen");
	}
	
	protected void clickAddedButtonInfoScreen() {
		clickElement(addedInfoScreenButton);;
	}
	
	protected void verifyAddedButtonInforScreen() {
		Assert.assertTrue(elementExists(addedInfoScreenButton, 40), "Added button in VAS info screen is not displayed");
	}
	
	protected void verifyCounterButtonInforScreen() {
		Assert.assertTrue(getElementCount(CountersInfoScreenButton)==3, "Counter button in VAS info screen is not displayed");
	}
	
	protected void clickContinue() {
		clickElement(continueButton);;
	}
	
	protected void clickNoThankYou() {
		scrollToElementText("Thank You");
		clickElement(noThankYouButton);;
	}
	
	
}
