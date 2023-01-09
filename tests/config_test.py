from commit_check import PASS, FAIL
from commit_check.config import check_git_config

# The location of check_git_config()
LOCATION = "commit_check.config"


class TestConfig:
    class TestAuthorName:
        # used by get_commits_info mock
        fake_config_value_an = "fake_author_name"

        def test_check_git_config(self, mocker):
            # Must call get_commits_info, re.match.
            checks = [{
                "check": "author_name",
                "regex": "dummy_regex"
            }]
            m_get_commits_info = mocker.patch(
                f"{LOCATION}.get_commits_info",
                return_value=self.fake_config_value_an
            )
            m_re_match = mocker.patch(
                "re.match",
                return_value="fake_rematch_resp"
            )

            res = check_git_config(checks, "author_name")

            assert res == PASS
            assert m_get_commits_info.call_count == 1
            assert m_re_match.call_count == 1

        def test_check_git_config_with_empty_checks(self, mocker):
            # Must NOT call get_commits_info, re.match. with `checks` param with length 0.
            checks = []
            m_get_commits_info = mocker.patch(
                f"{LOCATION}.get_commits_info",
                return_value=self.fake_config_value_an
            )
            m_re_match = mocker.patch(
                "re.match",
                return_value="fake_author_name"
            )

            res = check_git_config(checks, "author_name")

            assert res == PASS
            assert m_get_commits_info.call_count == 0
            assert m_re_match.call_count == 0

        def test_check_git_config_with_different_check(self, mocker):
            # Must NOT call get_commit_info, re.match with not `author_name`.
            checks = [{
                "check": "commit_message",
                "regex": "dummy_regex"
            }]
            m_get_commits_info = mocker.patch(
                f"{LOCATION}.get_commits_info",
                return_value=self.fake_config_value_an
            )
            m_re_match = mocker.patch(
                "re.match",
                return_value="fake_author_name"
            )

            res = check_git_config(checks, "author_name")

            assert res == PASS
            assert m_get_commits_info.call_count == 0
            assert m_re_match.call_count == 0

        def test_check_git_config_with_len0_regex(self, mocker, capfd):
            # Must NOT call get_commits_info, re.match with `regex` with length 0.
            checks = [
                {
                    "check": "author_name",
                    "regex": ""
                }
            ]
            m_get_commits_info = mocker.patch(
                f"{LOCATION}.get_commits_info",
                return_value=self.fake_config_value_an
            )
            m_re_match = mocker.patch(
                "re.match",
                return_value="fake_rematch_resp"
            )

            res = check_git_config(checks, "author_name")

            assert res == PASS
            assert m_get_commits_info.call_count == 0
            assert m_re_match.call_count == 0
            out, _ = capfd.readouterr()
            assert "Not found regex for author_name." in out

        def test_check_git_config_with_result_none(self, mocker):
            # Must call print_error_message, print_suggestion when re.match returns NONE.
            checks = [{
                "check": "author_name",
                "regex": "dummy_regex",
                "error": "error",
                "suggest": "suggest"
            }]
            m_get_commits_info = mocker.patch(
                f"{LOCATION}.get_commits_info",
                return_value=self.fake_config_value_an
            )
            m_re_match = mocker.patch(
                "re.match",
                return_value=None
            )
            m_print_error_message = mocker.patch(
                f"{LOCATION}.print_error_message"
            )
            m_print_suggestion = mocker.patch(
                f"{LOCATION}.print_suggestion"
            )

            res = check_git_config(checks, "author_name")

            assert res == FAIL
            assert m_get_commits_info.call_count == 1
            assert m_re_match.call_count == 1
            assert m_print_error_message.call_count == 1
            assert m_print_suggestion.call_count == 1

    class TestAuthorEmail:
        # used by get_commits_info mock
        fake_config_value_ae = "fake_author_email"

        def test_check_git_config(self, mocker):
            # Must call get_commits_info, re.match.
            checks = [{
                "check": "author_email",
                "regex": "dummy_regex"
            }]
            m_get_commits_info = mocker.patch(
                f"{LOCATION}.get_commits_info",
                return_value=self.fake_config_value_ae
            )
            m_re_match = mocker.patch(
                "re.match",
                return_value="fake_rematch_resp"
            )

            res = check_git_config(checks, "author_email")

            assert res == PASS
            assert m_get_commits_info.call_count == 1
            assert m_re_match.call_count == 1

        def test_check_git_config_with_empty_checks(self, mocker):
            # Must NOT call get_commits_info, re.match. with `checks` param with length 0.
            checks = []
            m_get_commits_info = mocker.patch(
                f"{LOCATION}.get_commits_info",
                return_value=self.fake_config_value_ae
            )
            m_re_match = mocker.patch(
                "re.match",
                return_value="fake_author_email"
            )

            res = check_git_config(checks, "author_email")

            assert res == PASS
            assert m_get_commits_info.call_count == 0
            assert m_re_match.call_count == 0

        def test_check_git_config_with_different_check(self, mocker):
            # Must NOT call get_commit_info, re.match with not `author_email`.
            checks = [{
                "check": "commit_message",
                "regex": "dummy_regex"
            }]
            m_get_commits_info = mocker.patch(
                f"{LOCATION}.get_commits_info",
                return_value=self.fake_config_value_ae
            )
            m_re_match = mocker.patch(
                "re.match",
                return_value="fake_author_email"
            )

            res = check_git_config(checks, "author_email")

            assert res == PASS
            assert m_get_commits_info.call_count == 0
            assert m_re_match.call_count == 0

        def test_check_git_config_with_len0_regex(self, mocker, capfd):
            # Must NOT call get_commits_info, re.match with `regex` with length 0.
            checks = [
                {
                    "check": "author_email",
                    "regex": ""
                }
            ]
            m_get_commits_info = mocker.patch(
                f"{LOCATION}.get_commits_info",
                return_value=self.fake_config_value_ae
            )
            m_re_match = mocker.patch(
                "re.match",
                return_value="fake_rematch_resp"
            )

            res = check_git_config(checks, "author_email")

            assert res == PASS
            assert m_get_commits_info.call_count == 0
            assert m_re_match.call_count == 0
            out, _ = capfd.readouterr()
            assert "Not found regex for author_email." in out

        def test_check_git_config_with_result_none(self, mocker):
            # Must call print_error_message, print_suggestion when re.match returns NONE.
            checks = [{
                "check": "author_email",
                "regex": "dummy_regex",
                "error": "error",
                "suggest": "suggest"
            }]
            m_get_commits_info = mocker.patch(
                f"{LOCATION}.get_commits_info",
                return_value=self.fake_config_value_ae
            )
            m_re_match = mocker.patch(
                "re.match",
                return_value=None
            )
            m_print_error_message = mocker.patch(
                f"{LOCATION}.print_error_message"
            )
            m_print_suggestion = mocker.patch(
                f"{LOCATION}.print_suggestion"
            )

            res = check_git_config(checks, "author_email")

            assert res == FAIL
            assert m_get_commits_info.call_count == 1
            assert m_re_match.call_count == 1
            assert m_print_error_message.call_count == 1
            assert m_print_suggestion.call_count == 1
            assert m_print_suggestion.call_count == 1