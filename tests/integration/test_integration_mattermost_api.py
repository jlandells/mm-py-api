import unittest
import os
import pytest
from mattermost_api.mattermost_api import make_mattermost_api_call


@pytest.mark.integration
class TestIntegrationMattermostAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Test Mattermost server details from environment variables
        cls.mattermost_url = os.getenv("MATTERMOST_TEST_URL", "http://localhost")
        cls.api_token = os.getenv("MATTERMOST_TEST_TOKEN", "")
        cls.port = int(os.getenv("MATTERMOST_TEST_PORT", 8065))
        cls.test_team_name = os.getenv("MATTERMOST_TEST_TEAM", "integration-testing")  # Replace with your team name
        cls.test_channel_name = os.getenv("MATTERMOST_TEST_CHANNEL", "test")  # Replace with your channel name

    def get_team_id(self, team_name):
        """Get the ID of a team by its name."""
        response = make_mattermost_api_call(
            mattermost_url=self.mattermost_url,
            api_token=self.api_token,
            endpoint="/api/v4/teams",
            method="GET",
            port=self.port,
        )
        for team in response:
            if team["name"] == team_name:
                return team["id"]
        raise RuntimeError(f"Team '{team_name}' not found")

    def get_channel_id(self, team_id, channel_name):
        """Get the ID of a channel by its name within a team."""
        response = make_mattermost_api_call(
            mattermost_url=self.mattermost_url,
            api_token=self.api_token,
            endpoint=f"/api/v4/teams/{team_id}/channels",
            method="GET",
            port=self.port,
        )
        for channel in response:
            if channel["name"] == channel_name:
                return channel["id"]
        raise RuntimeError(f"Channel '{channel_name}' not found in team '{team_id}'")

    def test_create_post(self):
        # Fetch the team ID
        team_id = self.get_team_id(self.test_team_name)

        # Fetch the channel ID
        channel_id = self.get_channel_id(team_id, self.test_channel_name)

        # Create a post in the channel
        response = make_mattermost_api_call(
            mattermost_url=self.mattermost_url,
            api_token=self.api_token,
            endpoint="/api/v4/posts",
            method="POST",
            port=self.port,
            json_body={
                "channel_id": channel_id,
                "message": "Hello, this is a test post!",
            },
        )
        self.assertIn("id", response)
        self.assertEqual(response["message"], "Hello, this is a test post!")

        # Cleanup: Delete the post
        post_id = response["id"]
        make_mattermost_api_call(
            mattermost_url=self.mattermost_url,
            api_token=self.api_token,
            endpoint=f"/api/v4/posts/{post_id}",
            method="DELETE",
            port=self.port,
        )


if __name__ == "__main__":
    unittest.main()
