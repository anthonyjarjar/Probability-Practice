from flask import Flask, jsonify, request, session, render_template
from blackjack import BlackJack
import json

app = Flask(__name__)
app.secret_key = "your_secret_key"


@app.route("/")
def home():
    return render_template("game.html")


@app.route("/start", methods=["GET", "POST"])
def start_game():
    if request.method == "POST":
        game = BlackJack()
        session["game_state"] = game.serialize_state()
        return jsonify(message="Game started"), 200
    return render_template("start_game.html")


def get_game_from_session():
    game_state = session.get("game_state", None)
    if game_state is not None:
        game = BlackJack.deserialize_state(game_state)
        return game
    return None


@app.route("/hit", methods=["POST"])
def hit():
    game = get_game_from_session()
    if game:
        game.hit()
        session["game_state"] = game.serialize_state()
        session.modified = True
        return (
            jsonify(
                success=True,
                player_hand=game.player.current_hand,
                game_over=game.calculate_hand() > 21,
            ),
            200,
        )
    return jsonify(error="Game not started"), 400


@app.route("/stand", methods=["POST"])
def stand():
    game = get_game_from_session()
    if game is not None:
        while game.calculate_house_hand() < 17:
            game.house_hit()
        session["game_state"] = game.serialize_state()
        session.modified = True

        player_score = game.calculate_hand()
        dealer_score = game.calculate_house_hand()
        result = (
            0
            if dealer_score > 21 or player_score > dealer_score
            else 1 if player_score < dealer_score else 2
        )

        return (
            jsonify(
                success=True,
                player_hand=game.player.current_hand,
                dealer_hand=game.house.current_hand,
                result=result,
                player_score=player_score,
                dealer_score=dealer_score,
            ),
            200,
        )
    else:
        return jsonify(error="No active game"), 400


if __name__ == "__main__":
    app.run(debug=True)
