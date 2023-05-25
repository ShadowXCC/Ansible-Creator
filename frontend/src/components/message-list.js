import React, { Component } from 'react';
import MessageView from './message-view-3';

class MessageList extends Component {
  state = {
    messages:  [
      {
        _id: 'd2504a54',
        from: 'John',
        content: 'The event will start next week',
        status: 'unread'
      },
      {
        _id: 'fc7cad74',
        from: 'Martha',
        content: 'I will be traveling soon',
        status: 'read'
      },
      {
        _id: '876ae642',
        from: 'Jacob',
        content: 'Talk later. Have a great day!',
        status: 'read'
      }
    ]
  }

  render() {
    const messageViews = this.state.messages.map(
      message => <MessageView key={message._id} message={message} />
    )

    return(
      <div className="container">
        <h1>List of Messages</h1>
        {messageViews}
      </div>
    )
  }
}

export default MessageList;