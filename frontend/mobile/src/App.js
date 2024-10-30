import React from 'react';
import { Text, StyleSheet, View } from 'react-native';

export default function App() {
  return (
    <View style={appStyles.container}>
      <Text style={appStyles.text}>Hello There!</Text>
    </View>
  );
}


const appStyles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#f5fcff',
  },
  text: {
    fontSize: 20,
    color: '#333333',
    textAlign: 'center',
    margin: 10,
  },
})