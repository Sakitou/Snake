const canvas = document.getElementById("gameCanvas");
const context = canvas.getContext("2d");

const blockSize = 20; // Increases block size
const snakeSpeed = 150; // Sets snake speed

// Calculate number of blocks in width and height
const numBlocksWidth = canvas.width / blockSize;
const numBlocksHeight = canvas.height / blockSize;

let snakeBody;
let snakeLength;
let foodX;
let foodY;
let direction;
let lastTime;

document.addEventListener("keydown", changeDirection);

function initialize() {
    snakeBody = [{x: 10, y: 10}];
    snakeLength = 1;
    direction = {x: 0, y: 0};
    placeFood();
    lastTime = 0;
}

function placeFood() {
    foodX = Math.floor(Math.random() * (canvas.width / blockSize)) * blockSize;
    foodY = Math.floor(Math.random() * (canvas.height / blockSize)) * blockSize;
}

function draw() {
    context.clearRect(0, 0, canvas.width, canvas.height);

    // Draw snake
    context.fillStyle = "#ffffff";
    snakeBody.forEach((segment) => {
        context.fillRect(segment.x, segment.y, blockSize, blockSize);
    });

    // Draw food
    context.fillStyle = "#00ff00";
    context.fillRect(foodX, foodY, blockSize, blockSize);

    // Draw score
    context.fillStyle = "#ffffff";
    context.font = "20px Arial";
    context.fillText("Score: " + (snakeLength - 1), 10, 20);
}

function headCollision() {
    return snakeBody.slice(1).some((segment) => {
        return segment.x === snakeBody[0].x && segment.y === snakeBody[0].y;
    });
}

function update(currentTime) {
    const timeElapsed = currentTime - lastTime;

    if (timeElapsed > snakeSpeed) {
        lastTime = currentTime;

        const newHead = {x: snakeBody[0].x + direction.x, y: snakeBody[0].y + direction.y};
        snakeBody.unshift(newHead);

        // Check collision with food
        if (newHead.x < foodX + blockSize &&
            newHead.x + blockSize > foodX &&
            newHead.y < foodY + blockSize &&
            newHead.y + blockSize > foodY) {
            placeFood();
            snakeLength++;
        } else {
            snakeBody.pop();
        }

        if (headCollision() || newHead.x < 0 || newHead.x >= canvas.width || newHead.y < 0 || newHead.y >= canvas.height) {
            initialize();
        }
    }

    draw(); // Draw on each update
    requestAnimationFrame(update); // Continue game loop
}

function changeDirection(event) {
    const keyPressed = event.keyCode;
    switch(keyPressed) {
        case 37: // Left arrow key
            if (direction.x !== blockSize) {
                direction = {x: -blockSize, y: 0};
            }
            break;
        case 38: // Up arrow key
            if (direction.y !== blockSize) {
                direction = {x: 0, y: -blockSize};
            }
            break;
        case 39: // Right arrow key
            if (direction.x !== -blockSize) {
                direction = {x: blockSize, y: 0};
            }
            break;
        case 40: // Down arrow key
            if (direction.y !== -blockSize) {
                direction = {x: 0, y: blockSize};
            }
            break;
    }
}

initialize();
requestAnimationFrame(update);
