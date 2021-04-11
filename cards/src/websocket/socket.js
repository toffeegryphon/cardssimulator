import { io } from "socket.io-client"

// const url = 'ws://0.0.0.0:8080'
const url = 'wss://hackillinois-cards.herokuapp.com'
const options = {}

export const socket = io(url, options)

socket.on('connect', () => {
  // joinRoom('abcd')
})

export function joinRoom(name, rid, update) {
  const data = { name, rid }
  socket.emit('join', data, (response) => {
    update(response)
  })
}

export function initialize(rid) {
  const data = { rid }
  socket.emit('initialize', data)
}

export function playCard(cardId, rid, update) {
  const data = { target: '_field', value: [cardId], rid }
  socket.emit('play', data, (response) => {
    update(response)
  })
}

export function drawCards(count, rid, update) {
  const data = { count, rid }
  socket.emit('draw', data, (response) => {
    update(response)
  })
}

export function dealCards(count, rid) {
  const data = { count, rid }
  socket.emit('deal', data)
}
