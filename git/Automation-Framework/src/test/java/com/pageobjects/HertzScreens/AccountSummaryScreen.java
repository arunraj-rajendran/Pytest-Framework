package com.pageobjects.HertzScreens;

import org.openqa.selenium.By;
import org.testng.Assert;

import com.framework.reusable.MobileResuableComponents;

public class AccountSummaryScreen extends MobileResuableComponents {

	By newMemberNumberLabelText = By.id("io.hertz.digital.qa:id/gpr_member_id");
	By logoutLinkText = By.id("io.hertz.digital.qa:id/text_logout");
	By loginFromAccountSummaryBtn = By.id("io.hertz.digital.qa:id/button_gpr_login");

	public AccountSummaryScreen() {
		super();
	}

	protected void verifyAccountSummaryScreenDisplayed() {
		Assert.assertTrue(elementExists(newMemberNumberLabelText, 5), "Account summary screen is not displayed");
	}

	protected void doLogOut() {
		clickElement(logoutLinkText);
	}

	protected void verifyAccountSummaryLoginScreenDisplayed() {
		Assert.assertTrue(elementExists(loginFromAccountSummaryBtn, 5),
				"Account summary Log in screen is not displayed");
	}

}
