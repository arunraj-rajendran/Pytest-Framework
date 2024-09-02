@AndroidShopAndBookRegression
Feature: Andriod Mobile App Testing
  As a user, I want to be able to login to the Android hetz mobile app with different member users of varios tires
  
  @Android @LogINAndLogOut
  Scenario Outline: Verify Login with different member tiers
  	Given user launches the Hertz app and enters Username: "<username>" and Password: "<password>"
  	When user clicks on Log in button in Log In Screen
  	Then verify Home screen is displayed
  	And verify Member tier displayed is same as: "<memberTier>" in Home screen
    
    Examples: 
      | username |	password	|	memberTier	|
      | 29289797 |	Test#123	|	Five Star	|
      | 29289798 |	Test#123	|	President's Circle	|
      | 29289799 |	Test#123	|	Platinum	|
      | 29289800 |	Test#123	|	Regular Gold	|
      

  @Android @LogINAndLogOut
  Scenario Outline: Verify LogOut
  	Given user launches the Hertz app and enters Username: "<username>" and Password: "<password>"
  	When user clicks on Log in button in Log In Screen
  	Then verify Home screen is displayed
  	When user clicks on Menu icon in Home screen
  	And user clicks on Account Summary link from navigation menu in Home screen
  	Then Account Summary screen is displayed
  	When user clicks on Log Out in Account Summary screen
  	Then verify Log in button is displayed in Account summary Screen
  	
    Examples: 
      | username   |	password	|
      | 29289797 	 |	Test#123	|