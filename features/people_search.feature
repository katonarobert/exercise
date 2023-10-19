Feature: Query information for People

    The user should be able to search for phrases and get matching results for people.

    Scenario Outline: Search for people and verify matching result endpoints
        Given The user wants to search for "people"
        When The user searches for phrase: "<search phrase>"
        Then Verify that the response code is "200"
        And Verify that the response body matches schema
        And Verify that search field contains search phrase: "<search phrase>"
        And Verify result endpoints for "films"
        And Verify result endpoints for "species"
        And Verify result endpoints for "vehicles"
        And Verify result endpoints for "starships"
        And Verify that the detailed entry is correct

        Examples: People
            | search phrase |
            | Luke          |
            | r2            |
            | Dar           |
            | Ob            |
            | asdfghjkl     |
