Feature: Query information for Planets

    The user should be able to search for phrases and get matching results for planets.

    Scenario Outline: Search for planets and verify matching result endpoints
        Given The user wants to search for "planets"
        When The user searches for phrase: "<search phrase>"
        Then Verify that the response code is "200"
        And Verify that the response body matches schema
        And Verify that search field contains search phrase: "<search phrase>"
        And Verify result endpoints for "residents"
        And Verify result endpoints for "films"
        And Verify that the detailed entry is correct

        Examples: Planets
            | search phrase |
            | Tatooine      |
            | Dagobah       |
            | Mi            |
            | asdfghjkl     |
