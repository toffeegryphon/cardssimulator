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

export function playCard(cardId, rid, update) {
  const data = { target: '_field', value: [cardId], rid }
  socket.emit('play', data, (response) => {
    update(response)
  })
}

// socket.on('update', (data) => {
 // console.log(data)
// })
