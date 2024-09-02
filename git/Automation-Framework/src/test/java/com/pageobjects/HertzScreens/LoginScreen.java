package com.pageobjects.HertzScreens;

import org.openqa.selenium.By;

import com.framework.reusable.MobileResuableComponents;

public class LoginScreen extends MobileResuableComponents {

	By usernameTxtbox = By
			.xpath("//android.widget.TextView[@text='Member ID or username']/../parent::android.widget.EditText");
	By passwordTxtbox = By.xpath("//android.widget.TextView[@text='Password']/../parent::android.widget.EditText");
	By loginBtn = By.xpath("//*[@text = 'Log in']/following-sibling::android.widget.Button");
	By doNotEnableBiametricLink = By.xpath("//android.widget.TextView[contains(@text,'Do not enable')]");
	By serviceIssueText = By.xpath("//android.widget.TextView[contains(@text,'service issue')]");

	public LoginScreen() {
		super();
	}

	protected void doEnterCredentials(String username, String password) {
		waitUntilElementVisible(usernameTxtbox, 60);
		enterText(usernameTxtbox, username);
		enterText(passwordTxtbox, password);
	}

	protected void doClickLogin() {
		clickElement(loginBtn);
		verifyServiceIssue();
		doClickDoNotEnableBiometric();
	}
	
	protected void doClickDoNotEnableBiometric() {
		if(elementExists(doNotEnableBiametricLink, 30))
			clickElement(doNotEnableBiametricLink);
	}
	
	protected void verifyServiceIssue() {
		for(int i=1; i<=1; i++)
		{
			if(elementExists(serviceIssueText, 30))
				clickElement(loginBtn);
		}
	}

}
