// import { io } from "socket.io-client"

const url = 'ws://localhost:1337'

export const socket = new WebSocket(url)

const test = { hello: 'world' }

socket.onopen = () => {
  socket.send(JSON.stringify(test))
}

socket.onmessage = (event) => {
  console.log(event)
}
