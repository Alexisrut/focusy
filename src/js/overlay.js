$(document).ready(function(){  
    var cardflipped = false;
    var currentcard = 0;
    var qanda = [];

    // Fetch incomplete tasks from your backend
    async function getIncompleteTasks() {
        try {
            const response = await fetch('https://super-space-fortnight-gv9gqjqxqxph9q59.github.dev/api/incomplete_task/{$tg_user.id}', {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${localStorage.getItem('token')}`
                }
            });
            const tasks = await response.json();
            qanda = tasks.map(task => ({
                id: task.id,
                q: task.task_word,
                correct: task.task_correct,
                incorrect: task.task_incorrect,
                explain: task.task_explain
            }));
            sessionLoaded();
        } catch (error) {
            console.error('Error fetching tasks:', error);
        }
    }

    // Initialize session
    function sessionLoaded() {
        if(qanda.length === 0) {
            finishSession();
            return;
        }
        
        $("#session-current-card .session-card-front .session-card-inner-text").html(qanda[0].q);
        $("#session-current-card .session-card-back .session-card-inner-text").html(qanda[0].correct);
        $("#session-current-card .session-card-back .session-card-explain").html(qanda[0].explain);
        
        window.setTimeout(function(){
            $("#session-wrapper").addClass("session-wrapper-loaded");
            $("#session-current-card").removeClass("session-card-preload"); 
        }, 100);
    }

    // Mark task as completed in your database
    async function markTaskCompleted(taskId) {
        try {
            await fetch(`/api/tasks/${taskId}/complete`, {
                method: 'POST',
                headers: {
                    'Authorization': `Bearer ${localStorage.getItem('token')}`
                }
            });
        } catch (error) {
            console.error('Error marking task complete:', error);
        }
    }

    // Event handlers
    $(document).on("click", "#session-close-card, #finish-button", endSession);

    $(document).on("click", ".session-card-know", async function(){
        if (!cardflipped) {
            cardflipped = true;
            flipCard();
        } else {
            await markTaskCompleted(qanda[currentcard].id);
            nextCard();
        }
    });

    $(document).on("click", ".session-card-forgot", function(){
        if (!cardflipped) {
            cardflipped = true;
            flipCard();
        } else {
            nextCard();
        }
    });

    function flipCard() {
        $(".session-card-wrapper").addClass('is-flipped');
        currentcard++;
    }

    function nextCard() {
        cardflipped = false;
        if(currentcard < qanda.length) {
            $("#session-current-card .session-card-front .session-card-inner-text").html(qanda[currentcard].q);
            $("#session-current-card .session-card-back .session-card-inner-text").html(qanda[currentcard].correct);
            $("#session-current-card .session-card-back .session-card-explain").html(qanda[currentcard].explain);
            $(".session-card-wrapper").removeClass('is-flipped');
        } else {
            finishSession();
        }
    }

    function finishSession() {
        $("#session-current-card").hide();
        $("#session-wrap-finished").show();
    }

    function endSession() {
        window.close();
    }

    // Start the session
    getIncompleteTasks();
});