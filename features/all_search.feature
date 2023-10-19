Feature: Query information for All 4 categories

    The user should be able to search for phrases and get matching results for all categories in 1 go.

    Scenario Outline: Search for all categories and verify matching result endpoints
        Given The user wants to search for "all"
        When The user searches for phrase: "<search phrase>"
        Then Verify that the response code is "200"
        And Verify that the response body matches schema
        And Verify that search field contains search phrase: "<search phrase>"
        And Verify result endpoints for "films"
        And Verify result endpoints for "residents"
        And Verify result endpoints for "pilots"
        And Verify result endpoints for "species"
        And Verify result endpoints for "vehicles"
        And Verify result endpoints for "starships"

        Examples: Phrases
            | search phrase |
            | Luke          |
            | fighter       |
            | Wi            |
            | asdfghjkl     |
