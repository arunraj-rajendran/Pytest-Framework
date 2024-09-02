package com.cucumber.steps.HertzScreens;

import com.pageobjects.HertzScreens.ReviewDetailsScreen;

import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;

public class ReviewDetailsScreenSteps extends ReviewDetailsScreen{
	
	@Then("verify Review Details Screen is displayed")
	public void verify_Review_Details_screen_displayed() {
		verifyReviewDetailsScreenDisplayed();
	}
	
	@When("user click on Book Now button in Review details screen")
	public void click_on_BookNow() {
		clickBookNow();
	}
}
