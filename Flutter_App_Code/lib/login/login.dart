import 'package:flutter/material.dart';
import 'package:flutter_login_template/flutter_login_template.dart';

class LoginScreen extends StatefulWidget {
  const LoginScreen({Key? key}) : super(key: key);

  @override
  State<LoginScreen> createState() => _LoginScreen();
}

enum _State {
  signIn,
  confirm,
  create,
}

class _LoginScreen extends State<LoginScreen> {
  late LoginTemplateStyle style;
  _State state = _State.signIn;

  @override
  void initState() {
    style = LoginTemplateStyle.defaultTemplate;
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    var logo = Image.asset(
      "splash.jpg",
      width: 80,
      height: 80,
    );

    var signInPage = LoginTemplateSignInPage(
      logo: logo,
      style: style,
      onPressedSignIn: () {


        //Sign in api calls here from the django webserver



      },
      onPressedSignUp: () {
        

        //Redirect to the django website from the application


      },
      onPressedForgot: () {
        

        // Redirect to forget password in the django website


      },
      socialButtons: [
        LoginTemplateSocialButton(
          text: 'Google',
          onPressed: () {

            //Google Login Activity Here


          },
          icon: Icon(
            Icons.android,
            size: 16,
            color: style.socialButtonTextStyle.color,
          ),
          style: style,
        )
      ],
      term: LoginTemplateTerm(
        style: style,
        onPressedTermOfService: () {

          // Terms and conditions with privacy policy generator.

        },
        onPressedPrivacyPolicy: () {

          //

        },
      ),
    );

    var signUpPage = LoginTemplateSignUpPage(
      logo: logo,
      style: style,
      onPressedSignIn: () {
        setState(() {
          state = _State.signIn;
        });
      },
      onPressedSignUp: () {
        setState(() {
          state = _State.confirm;
        });
      },
      term: LoginTemplateTerm(
        style: style,
        onPressedTermOfService: () {},
        onPressedPrivacyPolicy: () {},
      ),
    );

    var forgotPasswordPage = LoginTemplateForgotPasswordPage(
        logo: logo,
        style: style,
        onPressedNext: () {
          setState(() {
            state = _State.confirm;
          });
        });

    var confirmCodePage = LoginTemplateConfirmCodePage(
      logo: logo,
      style: style,
      onPressedNext: () {
        setState(() {
          state = _State.create;
        });
      },
      onPressedResend: () {},
    );

    var createPassword = LoginTemplateCreatePasswordPage(
      logo: logo,
      style: style,
      errorTextPassword: 'Wrong Password',
      onPressedNext: () {
        setState(() {
          state = _State.signIn;
        });
      },
    );

    Widget body;
    switch (state) {
      case _State.confirm:
        body = confirmCodePage;
        break;
      case _State.create:
        body = createPassword;
        break;
      default:
        body = signInPage;
        break;
    }

    return MaterialApp(
      title: 'Example',
      theme: ThemeData(
        primarySwatch: Colors.blue,
        accentColor: Colors.orangeAccent,
      ),
      home: Scaffold(
        appBar: AppBar(
          title: Text('Accident Prevention'),
        ),
        body: SingleChildScrollView(
          child: body,
        ),
      ),
    );
  }
}
