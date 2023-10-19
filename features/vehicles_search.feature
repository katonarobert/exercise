Feature: Query information for Vehicles

    The user should be able to search for phrases and get matching results for Vehicles.

    Scenario Outline: Search for vehicles and verify matching result endpoints
        Given The user wants to search for "vehicles"
        When The user searches for phrase: "<search phrase>"
        Then Verify that the response code is "200"
        And Verify that the response body matches schema
        And Verify that search field contains search phrase: "<search phrase>"
        And Verify result endpoints for "pilots"
        And Verify result endpoints for "films"
        And Verify that the detailed entry is correct

        Examples: Vehicles
            | search phrase   |
            | Sand Crawler    |
            | t-47 airspeeder |
            | fighter         |
            | asdfghjkl       |
