let find_index = (li: list('a), x: 'a) : int => {
  Js.log(li);
  Js.log(x);
  let result: int = [%bs.raw {| li.findIndex(x) |}];
  result;
};

let cheap_shuffle = (li: array('a)) : array('a) => {
  Js.log(li);
  %bs.raw
  {| li.sort(() => Math.random() - 0.5) |};
};

type result =
  | Win
  | Lose
  | Same;

let cardsDef = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2];

let cardHolder =
  cardsDef |> List.map(x => [x, x, x, x]) |> List.flatten |> Array.of_list;

let compare = (field, hand) : result => {
  let fieldPower = cardsDef |> find_index(field);
  let handPower = cardsDef |> find_index(hand);
  if (fieldPower === handPower) {
    Same;
  } else if (fieldPower > handPower) {
    Lose;
  } else {
    Win;
  };
};

let dealCards = () => cardHolder |> cheap_shuffle;
