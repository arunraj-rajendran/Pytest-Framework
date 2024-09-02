package com.cucumber.steps.HertzScreens;

import com.pageobjects.HertzScreens.AccountSummaryScreen;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;

public class AccountSummaryScreenSteps extends AccountSummaryScreen {

	@Then("Account Summary screen is displayed")
	public void verify_home_screen_displayed() {
		verifyAccountSummaryScreenDisplayed();
	}

	@When("user clicks on Log Out in Account Summary screen")
	public void click_on_logOut() {
		doLogOut();
	}

	@Then("verify Log in button is displayed in Account summary Screen")
	public void verify_accountsummary_login_Screen_displayed() {
		verifyAccountSummaryLoginScreenDisplayed();
	}

}
