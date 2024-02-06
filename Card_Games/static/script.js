$(document).ready(function() {
    function updateHand(handElement, cards) {
        handElement.empty(); 
        cards.forEach(card => {
            handElement.append(`<p>${card[0]} of ${card[1]}</p>`); 
        });
    }

    function gameOver(message) {
        alert(message);
        window.location.reload(); 
    }

    $('#hitButton').click(function() {
        $.ajax({
            url: '/hit',
            type: 'POST',
            success: function(response) {
                console.log("Hit response:", response);
                updateHand($('#playerHand'), response.player_hand);
                if (response.game_over) {
                    gameOver('Bust! Game over.');
                }
            },
            error: function(error) {
                console.log("Error on hit:", error); 
            }
        });
    });

    $('#standButton').click(function() {
        $.ajax({
            url: '/stand',
            type: 'POST',
            success: function(response) {
                console.log("Stand response:", response); 
                updateHand($('#playerHand'), response.player_hand);
                updateHand($('#dealerHand'), response.dealer_hand);
                let message = response.result === 0 ? 'You win!' : response.result === 1 ? 'Dealer wins!' : 'It\'s a tie!';
                gameOver(message);
            },
            error: function(error) {
                console.log("Error on stand:", error);
            }
        });
    });
});
