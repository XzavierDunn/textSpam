const sysEvents = Application("System Events");
const mes = Application("Messages");

let args = $.NSProcessInfo.processInfo.arguments;
let argv = [];
let argc = args.count;
for (let i = 4; i < argc; i++) {
  argv.push(ObjC.unwrap(args.objectAtIndex(i)));
}

let number = argv[0];
let message = argv[1];

const sendNewMessage = (number, message) => {
  mes.activate();
  delay(0.2);

  sysEvents.keystroke("n", { using: "command down" });
  sysEvents.keystroke(number);
  sysEvents.keyCode(36);
  sysEvents.keystroke(message);
  sysEvents.keyCode(36);
};

sendNewMessage(number, message);
