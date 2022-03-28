# Code Style

Between vertical alignment & hanging indent, which one should I choose? Compare the code blocks below:

Vertical Alignment:

```py
self.initial = nn.Sequential(nn.Conv2d(in_channels,
                                        features[0],
                                        kernel_size=4,
                                        stride=2,
                                        padding=1,
                                        padding_mode="reflect"),
                              nn.LeakyReLU(0.2, inplace=True))
```

Hanging indent:

```py
self.initial = nn.Sequential(
    nn.Conv2d(
        in_channels,
        features[0],
        kernel_size=4,
        stride=2,
        padding=1,
        padding_mode="reflect",
    ),
    nn.LeakyReLU(0.2, inplace=True),
)
```

Which one would be more consistent in the long term? Of course the hanging indent one.
