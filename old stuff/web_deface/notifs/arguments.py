# -*- coding: utf-8 -*-
import argparse


def get_args():
    """Docstring.

    Returns:
        Args: total arguments
    """
    parser = argparse.ArgumentParser(description='Risk Assessment Framework')

    parser.add_argument(
        '--twitter_api_key',
        '-tak',
        type=str,
        required=False,
        help='Twitter api key'
    )

    parser.add_argument(
        '--twitter_api_secret_key',
        '-tas',
        type=str,
        required=False,
        help='Twitter api secret'
    )

    parser.add_argument(
        '--twitter_access_token',
        '-tat',
        type=str,
        required=False,
        help='Twitter access token'
    )

    parser.add_argument(
        '--twitter_access_token_secret',
        '-tats',
        type=str,
        required=False,
        help='Twitter access token secret'
    )

    parser.add_argument(
        '--telegram_bot_token',
        '-tbt',
        type=str,
        required=False,
        help='Telegram Bot Token'
    )

    parser.add_argument(
        '--telegram_user_id',
        '-tui',
        type=str,
        required=False,
        help='Telegram user id'
    )

    parser.add_argument(
        '--twilio_sid',
        '-tws',
        type=str,
        required=False,
        help='Twilio SID'
    )

    parser.add_argument(
        '--twilio_token',
        '-twt',
        type=str,
        required=False,
        help='Twilio authorization token'
    )

    parser.add_argument(
        '--twilio_from',
        '-twf',
        type=str,
        required=False,
        help='Twilio (From) phone number'
    )

    parser.add_argument(
        '--twilio_to',
        '-twto',
        type=str,
        required=False,
        help='Twilio (To) phone number'
    )

    parser.add_argument(
        '--slack_token',
        '-st',
        type=str,
        required=False,
        help='Slack token'
    )

    parser.add_argument(
        '--slack_user_id',
        '-suid',
        type=str,
        required=False,
        help='Slack user id'
    )

    args = parser.parse_args()
    return args
