package com.cucumber.steps.HertzScreens;

import com.pageobjects.HertzScreens.LoginScreen;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.When;

public class LoginScreenSteps extends LoginScreen {

	@Given("user launches the Hertz app and enters Username: {string} and Password: {string}")
	public void user_launches_the_hertz_app_and_logs_in_with_username_and_password(String username, String password) {
		doEnterCredentials(username, password);
	}

	@When("user clicks on Log in button in Log In Screen")
	public void click_login() {
		doClickLogin();
	}

	@Given("user launches the Hertz app and Log In with Username: {string} and Password: {string}")
	public void login(String username, String password) {
		user_launches_the_hertz_app_and_logs_in_with_username_and_password(username, password);
		doClickLogin();
	}
}
