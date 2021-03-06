from schema import Schema, Optional, Or  # type: ignore

# https://github.com/keleshev/schema

create_game_client_schema = Schema(
    {
        "protocol_type": "create_game",
        "board_state": [[int]],
        "rules": str,
        Or("p1_account_id", "p2_account_id", only_one=True): int,
        Optional("ai_difficulty"): int,
    }
)

create_game_server_schema = Schema(
    {
        "protocol_type": "create_game",
        "success": bool,
        "game_id": int,
    }
)

save_game_client_schema = Schema(
    {
        "protocol_type": "save_game",
        "game_id": int,
        "complete": bool,
        "board_state": [[int]],
        "next_turn": int,
    }
)

save_game_server_schema = Schema(
    {
        "protocol_type": "save_game",
        "success": bool,
    }
)

save_preferences_client_schema = Schema(
    {
        "protocol_type": "save_preferences",
        "account_id": int,
        "pref_board_length": int,
        "pref_board_color": str,
        "pref_disk_color": str,
        "pref_opp_disk_color": str,
        "pref_line_color": str,
        "pref_rules": str,
        "pref_tile_move_confirmation": bool,
    }
)

save_preferences_server_schema = Schema(
    {"protocol_type": "save_preferences", "success": bool}
)

get_game_client_schema = Schema(
    {
        "protocol_type": "get_game",
        "account_id": int,
        "resume_game": bool,
    }
)

get_game_server_schema = Schema(
    {
        "protocol_type": "get_game",
        "success": bool,
        "game_id": int,
        "complete": bool,
        "board_state": [[int]],
        "rules": str,
        "next_turn": int,
        Optional("account1"): {
            "p1_account_id": int,
            "p1_username": str,
            "p1_elo": int,
        },
        Optional("account2"): {
            "p2_account_id": int,
            "p2_username": str,
            "p2_elo": int,
        },
        Optional("ai_difficulty"): int,
    }
)

update_elo_client_schema = Schema(
    {
        "protocol_type": "update_elo",
        "account_id": int,
        "new_elo": int,
    }
)

update_elo_server_schema = Schema(
    {
        "protocol_type": "update_elo",
        "success": bool,
    }
)

get_top_elos_client_schema = Schema(
    {
        "protocol_type": "get_top_elos",
        "num_elos": int,
    }
)

get_top_elos_server_schema = Schema(
    {
        "protocol_type": "get_top_elos",
        "success": bool,
        "top_elos": [[str, int]],
    }
)

credential_check_client_schema = Schema(
    {
        "protocol_type": "login",
        "username": str,
    }
)

credential_check_server_schema = Schema(
    {
        "protocol_type": "login",
        "success": bool,
        "encrypted_password": str,
        "account_id": int,
        "elo": int,
        "pref_board_length": int,
        "pref_board_color": str,
        "pref_disk_color": str,
        "pref_opp_disk_color": str,
        "pref_line_color": str,
        "pref_rules": str,
        "pref_tile_move_confirmation": bool,
    }
)

create_account_client_schema = Schema(
    {
        "protocol_type": "create_account",
        "username": str,
        "password": str,
        "elo": int,
        "pref_board_length": int,
        "pref_board_color": str,
        "pref_disk_color": str,
        "pref_opp_disk_color": str,
        "pref_line_color": str,
        "pref_rules": str,
        "pref_tile_move_confirmation": bool,
    }
)

create_account_server_schema = Schema(
    {
        "protocol_type": "create_account",
        "success": bool,
        "account_id": int,
    }
)

matchmaker_client_schema = Schema(
    {
        "protocol_type": "matchmaker",
        "my_account_id": int,
        "pref_rule": str,
        "pref_board_size": int,
    }
)

matchmaker_server_schema = Schema(
    {
        "protocol_type": "matchmaker",
        "success": bool,
        "game_id": int,
        "opp_username": str,
        "opp_elo": int,
        "player_term": int,
    }
)

cancel_match_client_schema = Schema(
    {
        "protocol_type": "cancel_match",
        "my_account_id": int,
    }
)

cancel_match_server_schema = Schema(
    {
        "protocol_type": "cancel_match",
        "success": bool,
    }
)
