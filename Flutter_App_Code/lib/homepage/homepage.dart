import 'package:flutter/material.dart';
import 'package:geolocator/geolocator.dart';
import 'package:adui/login/login.dart';

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'ADUI',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const MyHomePage(title: 'Flutter Demo Home Page'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  @override
  void initState() {
    navigateHome();
    super.initState();
  }

  double speed = 0;

  String latitude = "";
  String longitude = "";

  @override
  Widget build(BuildContext context) {
    Position position;
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        title: const Text(
          "Accident Prevention",
          style: TextStyle(color: Colors.white),
        ),
        backgroundColor: Colors.black,
      ),
      body: Center(
        child: Expanded(child: Image.asset("splash.jpg")),
      ),
    );
  }

  void handleLocationRequest() async {
    while (true) {
      await Future.delayed(const Duration(seconds: 5));

      Position position = await Geolocator.getCurrentPosition(
          desiredAccuracy: LocationAccuracy.high);

      latitude = position.latitude.toString();

      longitude = position.longitude.toString();

      speed = position.speed * 1.60934;

      Navigator.of(context)
          .push(MaterialPageRoute(builder: (context) => LoginScreen()));

      break;
      setState(() {
        {}
      });
    }
  }

  void navigateHome() async {
    await Future.delayed(const Duration(seconds: 5));
    Navigator.of(context)
        .push(MaterialPageRoute(builder: (context) => const LoginScreen()));
  }
}
