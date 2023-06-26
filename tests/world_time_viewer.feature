Feature: world time Viewer App

    Scenario: Lunch the app and display time in system timezone
        When user run the app
        Then the timezone of app set to the system timezone
        And the menu of timezone should be update and display system timezone
        And title label should be update and display The present time in system timezone
        And time label should be update and display the current time in system timezone

    Scenario Outline: Update Time when Selecting Timezone
        Given the App is launched
        When user selects a <timezone> from the timezone menu
        Then the app timezone set to the user-selected timezone <timezone>
        And the timezone menu should be update and display <timezone>
        And the title label should be update and display The present time in <timezone>
        And the time label should be update and display the current time in <timezone>

        Examples:
            | timezone |
            | JST      |
            | GMT      |
            | PST      |

    Scenario: Continuously Update Time
        Given the App is launched
        When the time passes
        Then the time label should be updated to reflect the current time in the app timezone

    Scenario: Close the App
        Given the App is launched
        When user click the close button
        Then the app should be closed
