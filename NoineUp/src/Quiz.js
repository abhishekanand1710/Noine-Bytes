import React , {Component} from 'react';
import { View, Text } from 'react-native';

export default class Quiz extends Component {
    static navigationOptions = {
        headerMode: 'none'
      }
    render()
    {
        return(
            <View>
                <Text>Quiz</Text>
            </View>
        )
    }

}