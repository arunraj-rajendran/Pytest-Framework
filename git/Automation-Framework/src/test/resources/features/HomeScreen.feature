@AndroidShopAndBookRegression
Feature: Andriod Mobile App Testing
  As a user, I want to be able to login to the Android hetz mobile app and the pick up, drop off date and time should be prepopulated
  
  @Android @HomeScreenValidations
  Scenario Outline: Verify default date and time selected for pick up and drop-off fields
  	Given user launches the Hertz app and Log In with Username: "<username>" and Password: "<password>"
  	Then verify Home screen is displayed
  	And verify Pick up date is set two weeks from today in Home screen
  	And verify Pick up time is set to 12:00 PM in Home screen
  	And verify drop-off date is set two weeks plus two days from today in Home screen
  	And verify drop-off time is set to 12:00 PM in Home screen
    
    Examples: 
      | username |	password	|	memberTier	|
      | 29289797 |	Test#123	|	Five Star	|
      
