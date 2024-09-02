package com.pageobjects.HertzScreens;

import org.openqa.selenium.By;
import org.testng.Assert;

import com.framework.reusable.MobileResuableComponents;

public class DiscountCodeInformationScreen extends MobileResuableComponents{

	By discountInfoTitle = By.xpath("//android.widget.TextView[@text='Discount code information']");
	By backNavigationDiscountInfo = By.xpath("//android.widget.TextView[contains(@text,'Discount code information')]/../android.view.View");
	By discountInfoCDP = By.xpath("//android.widget.TextView[@text='Corporate Discount Program (CDP)']");
	By discountInfoCDPContent = By.xpath("//android.widget.TextView[@text='Corporate Discount Program (CDP)']/../following-sibling::android.widget.TextView[contains(@text,'corporate rate plans')]");
	By discountInfoPC = By.xpath("//android.widget.TextView[@text='Promotional Coupon (PC)']");
	By discountInfoPCContent = By.xpath("//android.widget.TextView[@text='Promotional Coupon (PC)']/../following-sibling::android.widget.TextView[contains(@text,'special offer or promotion')]");
	By discountInfoRQ = By.xpath("//android.widget.TextView[@text='Rate Code (RQ)']");
	By discountInfoRQContent = By.xpath("//android.widget.TextView[@text='Rate Code (RQ)']/../following-sibling::android.widget.TextView[contains(@text,'specific rate plan')]");
	
	
	public DiscountCodeInformationScreen() {
		super();
	}
	
	protected void verifyDiscountCodeInfoScreenDisplayed() {
		Assert.assertTrue(elementExists(discountInfoTitle, 40), "Discount Code Info screen is not displayed");
	}
	
	protected void verifyDiscountInfoCDPSectionIsDisplayed() {
		Assert.assertTrue(elementExists(discountInfoCDP, 40), "Discount Code Info CDP Section is not displayed");
	}
	
	
	protected void ClickCDPInfo() {	
		clickElement(discountInfoCDP);
	}
	
	protected void verifyDiscountInfoCDPContent() {
		Assert.assertTrue(elementExists(discountInfoCDPContent, 40), "Discount Code CDP Info content is not displayed/Not correct");
	}
	
	
	protected void verifyDiscountInfoPCSectionIsDisplayed() {
		Assert.assertTrue(elementExists(discountInfoPC, 40), "Discount Code PC section is not displayed");
	}
	
	protected void ClickPCInfo() {
		clickElement(discountInfoPC);
	}
	
	protected void verifyDiscountInfoPCContent() {
		Assert.assertTrue(elementExists(discountInfoPCContent, 40), "Discount Code PC info content is not displayed/not correct");
	}
	
	protected void verifyDiscountInfoRQSectionIsDisplayed() {
		Assert.assertTrue(elementExists(discountInfoRQ, 40), "Discount Code RQ section is not displayed");
	}
	
	protected void ClickRQInfo() {
		clickElement(discountInfoRQ);
	}
	
	protected void verifyDiscountInfoRQContent() throws InterruptedException {
		Assert.assertTrue(elementExists(discountInfoRQContent, 40), "Discount Code RQ info content is not displayed/not correct");
	}
	
	
	protected void ClickBackNavigationDiscountInfo() throws InterruptedException {
		clickElement(backNavigationDiscountInfo);
	}

}
