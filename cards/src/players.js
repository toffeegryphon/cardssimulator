import React from 'react'

export default class Players extends React.Component {
  render() {
    const players = []
    for (const [sid, player] of Object.entries(this.props.players)) {
      players.push(<div key={sid}>{player.name} {player.count}</div>)
      // players.push(<div key={sid}>{sid} {player}</div>)
    }
    return (
      <div>{players}</div>
    )
  }
}
