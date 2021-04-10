import { io } from "socket.io-client"

const url = 'ws://0.0.0.0:8080'

export const socket = io(url)

socket.on('connect', () => {
  // joinRoom('abcd')
})

export function joinRoom(rid, update) {
  socket.emit('join', rid, (response) => {
    // console.log(response)
    update(response)
  })
}

