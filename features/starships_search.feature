Feature: Query information for Starships

    The user should be able to search for phrases and get matching results for Starships.

    Scenario Outline: Search for starships and verify matching result endpoints
        Given The user wants to search for "starships"
        When The user searches for phrase: "<search phrase>"
        Then Verify that the response code is "200"
        And Verify that the response body matches schema
        And Verify that search field contains search phrase: "<search phrase>"
        And Verify result endpoints for "pilots"
        And Verify result endpoints for "films"
        And Verify that the detailed entry is correct

        Examples: Starships
            | search phrase                   |
            | X-wing                          |
            | Imperial I-class Star Destroyer |
            | fighter                         |
            | asdfghjkl                       |
